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
        Factor Graph Belief Propagation (Decentralized Perceptual Inference).
        Instead of a top-down evaluation tracking all variables, nodes dynamically calculate 
        local prediction errors and pass 'messages' to immediate neighbors.
        This framework allows massive simultaneous parallelization on Apple M-Silicon GPUs.
        """
        # 1. Initialize local graph beliefs
        local_beliefs = {name: var.current_value for name, var in self.generative_model.variables.items()}
        for obs_key, obs_val in sensory_observations.items():
             if obs_key in local_beliefs:
                 local_beliefs[obs_key] = obs_val
                 
        # 2. Synchronous Message Passing Iteration (Simulating parallel Tensor propagation)
        max_iterations = 5
        for _ in range(max_iterations):
            new_beliefs = dict(local_beliefs)
            for name, var in self.generative_model.variables.items():
                # Observations and exogenous roots act as clamped anchor nodes
                if name in sensory_observations or var.is_exogenous:
                    continue 
                
                # Receive incoming state messages from parent Markov blanket
                parent_messages = {p.name: local_beliefs.get(p.name) for p in var.parents}
                if all(v is not None for v in parent_messages.values()):
                    # Local node update (computing factor equation)
                    new_val = var.compute(parent_messages)
                    new_beliefs[name] = new_val
                    
            if new_beliefs == local_beliefs: # Equilibrium converged
                break
            local_beliefs = new_beliefs
            
        # 3. Compute thermodynamic Surprise (Free Energy) over the converged state
        total_surprise = 0.0
        for name, var in self.generative_model.variables.items():
            if name in sensory_observations and name in local_beliefs:
                surprise = FreeEnergyCalculator.compute_surprise(local_beliefs[name], sensory_observations[name])
                total_surprise += surprise
            var.current_value = local_beliefs.get(name)
            
        self.current_free_energy = total_surprise
        return local_beliefs

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
