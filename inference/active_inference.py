"""
Active Inference Perception-Action Loop for SAGE

Implements the continuous dual-optimization loop defined by Karl Friston.
The agent updates beliefs (Perceptual Inference) and takes actions 
(Active Inference Action) to minimize prediction errors against its generative model.
"""

from typing import Dict, Any, List, Callable
from sage.inference.free_energy import FreeEnergyCalculator
from sage.causality.scm import SCM
from sage.causality.koopman import DynamicCausalSimulator
from sage.optimizations.mps_tensor_network import MatrixProductStateSearch

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
        
        # Phase 15 Dynamic Mathematics
        self.dynamic_simulator = DynamicCausalSimulator()
        self.tensor_network: MatrixProductStateSearch = None

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

    def act(self, available_actions: List[Dict[str, Any]], current_state: float = 1.0) -> Dict[str, Any]:
        """
        Active Inference (Action).
        The agent selects the action that minimizes Expected Free Energy (G).
        """
        best_action = None
        min_efe = float('inf')
        
        # 1. Prepare Tensor Network for topological evaluation
        variables = list(self.generative_model.variables.keys())
        self.tensor_network = MatrixProductStateSearch(variables)
        
        for action in available_actions:
            # 2. Continuous Koopman Intervention
            # We map the action to a target value for the Koopman operator
            action_val = 1.0 if "forward" in str(action) else 0.0
            predicted_state = self.dynamic_simulator.simulate_do_intervention(current_state, action_val)
            
            # 3. Categorical/MPS Confidence
            # How much does this action satisfy our primary homeostatic goal?
            # Assuming the first preference is our target
            goal_var = list(self.preferences.keys())[0] if self.preferences else "unknown"
            action_id = action.get("action_type", "unknown")
            confidence = self.tensor_network.evaluate_do_calculus(action_id, goal_var)
            
            # 4. Rigorous G-Calculation
            # Projects the outcomes into a probability distribution over the goal variable
            expected_outcomes = {
                goal_var: confidence,       # Alignment (Pragmatic)
                "ambiguity": 1.0 - confidence # Uncertainty (Epistemic)
            }
            
            # Calculate G = Risk + Ambiguity
            efe = FreeEnergyCalculator.expected_free_energy(expected_outcomes, self.preferences)
            
            if efe < min_efe:
                min_efe = efe
                best_action = action
                
        return best_action or {}
