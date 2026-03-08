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
    def expected_free_energy(expected_outcomes: Dict[str, float], preferences: Dict[str, float], ambiguity: float = 0.1) -> float:
        """
        Calculates Expected Free Energy (G) for action selection.
        G = Risk + Ambiguity
        
        Where:
        - Risk (Pragmatic Value): KL[Q(s|pi) || P(s)]
        - Ambiguity (Epistemic Value): H[Q(s|pi)] -- (Simplified as a curiosity factor)
        """
        risk = 0.0
        for state, prob in expected_outcomes.items():
            if state in preferences:
                # KL Divergence: expected vs preferred (Pragmatic)
                pref_prob = preferences[state]
                if prob > 0 and pref_prob > 0:
                    risk += prob * math.log(prob / pref_prob)
            else:
                # If the state is unknown, assume high surprise (Risk)
                risk += 1.0 
                
        # Epistemic Value (Inverted Ambiguity): 
        # Drives the agent to explore states with high uncertainty/ambiguity.
        # Here we subtract a curiosity term to lower G for novel/uncertain outcomes.
        epistemic_curiosity = -ambiguity * sum(p * math.log(p) if p > 0 else 0 for p in expected_outcomes.values())
        
        return risk + epistemic_curiosity
