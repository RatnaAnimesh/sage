"""
Free Energy Principle Math for SAGE

Implements the core thermodynamic equations of Karl Friston's Free Energy Principle.
The agent seeks to minimize variational free energy (an upper bound on surprise)
by updating its internal models or acting on the world to change sensory input.
"""

import math
from typing import Dict, Any

class FreeEnergyCalculator:
    """
    Computes Variational Free Energy bounds for the SAGE agent.
    """
    
    @staticmethod
    def compute_surprise(prediction: float, observation: float, variance: float = 1.0) -> float:
        """
        Calculates simple prediction error (Surprise).
        Assumes a Gaussian distribution for sensory noise for simplified computation.
        
        S = -ln P(Observation | Prediction)
          ∝ (Observation - Prediction)^2 / (2 * variance)
        """
        if variance <= 0:
            variance = 0.0001
        
        error = observation - prediction
        return (error ** 2) / (2 * variance)

    @staticmethod
    def expected_free_energy(action_expected_outcomes: Dict[str, float], desired_preferences: Dict[str, float]) -> float:
        """
        Calculates Expected Free Energy (G) for future planning.
        Used to select actions. Combines:
        1. Epistemic value (Exploration): reducing uncertainty.
        2. Pragmatic value (Exploitation): fulfilling homeostatic preferences.
        
        Simplified representation of: G ≈ Risk + Ambiguity
        """
        efe = 0.0
        for state, expected_prob in action_expected_outcomes.items():
            # Pragmatic Value: How well does this align with our goals?
            preference_prob = desired_preferences.get(state, 0.01) # Small prior if unstated
            
            # Risk/KL Divergence between expected outcomes and preferred outcomes
            if expected_prob > 0:
                efe += expected_prob * math.log(expected_prob / preference_prob)
                
            # Note: A full implementation would also calculate 'Ambiguity' here
            # to drive the agent to explore uncertain epistemic states.
            
        return efe
