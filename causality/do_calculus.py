"""
Do-Calculus Interventions for SAGE

Implements Judea Pearl's do() operator. This allows the AGI to 
simulate deliberate interventions in the environment, severing incoming 
causal arrows and asking counterfactual questions (Layer 2 & 3 of Causation).
"""

from typing import Any, Dict
from sage.causality.scm import SCM
import copy

class DoCalculus:
    """
    Handles the mathematical manipulation of SCMs for intervention.
    """
    
    @staticmethod
    def intervene(original_scm: SCM, interventions: Dict[str, Any]) -> SCM:
        """
        The do(X=x) operator.
        1. Copies the SCM graph.
        2. Deletes all incoming edges to variables in `interventions`.
        3. Sets their values constantly to `x`.
        """
        # Conceptually we duplicate the SCM to map a counterfactual universe SCM_do(X)
        mutated_scm = SCM(name=f"{original_scm.name}_do({list(interventions.keys())})")
        
        # Deep copy structure
        for name, var in original_scm.variables.items():
             new_var = copy.copy(var)
             # Reset connections for safe rebuilding
             new_var.parents = []
             new_var.children = []
             mutated_scm.add_variable(new_var)
             
        # Rebuild edges, omitting incoming arrows to intervened variables
        for name, var in original_scm.variables.items():
             if name in interventions:
                  # do(X=x) shears external influences
                  pass
             else:
                  for p in var.parents:
                       mutated_scm.add_causal_link(p.name, name)
                       
        # Set the forced values
        for name, fixed_val in interventions.items():
             if name in mutated_scm.variables:
                 mutated_scm.variables[name].is_exogenous = True
                 mutated_scm.variables[name].current_value = fixed_val
                 # Obliterate the structural equation, it is now a constant
                 mutated_scm.variables[name].structural_equation = lambda: fixed_val

        return mutated_scm

    @staticmethod
    def counterfactual(scm: SCM, past_evidence: Dict[str, Any], hypothesized_action: Dict[str, Any]) -> Dict[str, Any]:
        """
        Layer 3 Causation: "Given that Y=y happened when X=x, what WOULD have 
        happened if X=x'?"
        
        Algorithm:
        1. Abduction: Use past_evidence to estimate the exogenous noise variables U.
        2. Action: Apply the do(X=x') intervention to create a mutated SCM.
        3. Prediction: Evaluate the mutated SCM using the noise U from step 1.
        """
        # Step 1: Update the base SCM with evidence (Abduction phase simplified here)
        scm.evaluate(past_evidence)
        
        # Step 2: Mutilate the graph with the hypothesized action
        cf_scm = DoCalculus.intervene(scm, hypothesized_action)
        
        # Step 3: Forward inference in the counterfactual world
        # We start evaluation using the exogenous states derived in Step 1
        return cf_scm.evaluate({})
