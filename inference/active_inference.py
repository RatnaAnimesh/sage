"""
Active Inference Perception-Action Loop for SAGE

Implements the continuous dual-optimization loop defined by Karl Friston.
The agent updates beliefs (Perceptual Inference) and takes actions 
(Active Inference Action) to minimize prediction errors against its generative model.
"""

from typing import Dict, Any, List, Callable
from sage.inference.free_energy import FreeEnergyCalculator
from sage.causality.scm import SCM

class ActiveInferenceAgent:
    """
    The main thermodynamically-driven inference loop.
    Interacts with the world across a Markov blanket.
    """
    def __init__(self, generative_model: SCM, homeostatic_goals: Dict[str, float]):
        self.generative_model = generative_model
        
        # P(C): The prior distribution over preferred sensory states
        self.preferences = homeostatic_goals
        
        self.current_free_energy = 0.0

    def perceive(self, sensory_observations: Dict[str, float]) -> Dict[str, Any]:
        """
        Perceptual Inference (Updating Internal Beliefs).
        The agent attempts to explain the sensory observations using its generative model.
        """
        # 1. Forward pass on model without observations to get predictions
        predictions = self.generative_model.evaluate({})
        
        total_surprise = 0.0
        # 2. Compare predictions to actual observations
        for obs_key, obs_val in sensory_observations.items():
            if obs_key in predictions and predictions[obs_key] is not None:
                surprise = FreeEnergyCalculator.compute_surprise(predictions[obs_key], obs_val)
                total_surprise += surprise
                
        self.current_free_energy = total_surprise
        
        # 3. Update model using observations (Abduction/State inference)
        # Note: In a full continuous POMDP this involves gradient descent on Free Energy.
        # Here we do deterministic setting on the SCM
        inferred_states = self.generative_model.evaluate(sensory_observations)
        
        return inferred_states

    def act(self, available_actions: List[Dict[str, Any]], forward_simulate: Callable) -> Dict[str, Any]:
        """
        Active Inference (Action).
        The agent selects the action that minimizes Expected Free Energy (EFE) in the future.
        """
        best_action = None
        min_efe = float('inf')
        
        for action in available_actions:
            # 1. Simulate the future using the generative model + Do-Calculus
            # forward_simulate should use DoCalculus.counterfactual under the hood
            expected_outcomes = forward_simulate(self.generative_model, action)
            
            # 2. Calculate EFE (Risk + Ambiguity) relative to preferences
            efe = FreeEnergyCalculator.expected_free_energy(expected_outcomes, self.preferences)
            
            # 3. Select Action
            if efe < min_efe:
                min_efe = efe
                best_action = action
                
        return best_action or {}
