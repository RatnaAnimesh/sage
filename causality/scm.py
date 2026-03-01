"""
Structural Causal Models (SCM) for SAGE

Implements Judea Pearl's Directed Acyclic Graphs (DAGs) to map 
causal mechanisms rather than mere statistical correlations.
Nodes are random variables, edges represent structural equations.
"""

from typing import Any, Callable, Dict, List, Set, Optional

class CausalVariable:
    """
    A variable within the Structural Causal Model.
    Can be exogenous (determined outside the model) or 
    endogenous (determined by parents within the model).
    """
    def __init__(self, name: str, is_exogenous: bool = False):
        self.name = name
        self.is_exogenous = is_exogenous
        self.parents: List['CausalVariable'] = []
        self.children: List['CausalVariable'] = []
        # The structural equation: f(parents) -> value
        self.structural_equation: Optional[Callable[..., Any]] = None
        
        # Current inferred or observed state
        self.current_value: Any = None

    def add_parent(self, parent: 'CausalVariable') -> None:
        if parent not in self.parents:
            self.parents.append(parent)
            parent.children.append(self)

    def set_equation(self, eq: Callable[..., Any]) -> None:
        self.structural_equation = eq

    def compute(self, parent_values: Dict[str, Any]) -> Any:
        """Evaluates the variable based on its structural equation."""
        if self.is_exogenous or not self.structural_equation:
            return self.current_value
        return self.structural_equation(**parent_values)

    def __repr__(self) -> str:
        role = "Exogenous" if self.is_exogenous else "Endogenous"
        return f"<CausalVar({role}): {self.name}>"


class SCM:
    """
    The Structural Causal Model linking variables into a continuous DAG.
    SAGE uses this to distinguish causal relationships from correlation.
    """
    def __init__(self, name: str = "WorldModel_DAG"):
        self.name = name
        self.variables: Dict[str, CausalVariable] = {}

    def add_variable(self, var: CausalVariable) -> None:
        self.variables[var.name] = var

    def add_causal_link(self, cause_name: str, effect_name: str) -> None:
        cause = self.variables[cause_name]
        effect = self.variables[effect_name]
        effect.add_parent(cause)

    def evaluate(self, evidence: Dict[str, Any]) -> Dict[str, Any]:
        """
        Observational inference (Pearl's Layer 1).
        Given some observed variables, what are the expected values of the others?
        """
        # Note: A full SCM evaluator would do topological sorting and propagate noise.
        # This is the simplified deterministic skeleton.
        results = dict(evidence)
        for name, var in self.variables.items():
            if name in evidence:
                var.current_value = evidence[name]
            elif var.is_exogenous:
                 # In a real model, this would sample from a prior noise distribution P(U)
                 var.current_value = None 
            else:
                 parent_vals = {p.name: results.get(p.name) for p in var.parents}
                 # only compute if all parents are known
                 if all(v is not None for v in parent_vals.values()):
                     val = var.compute(parent_vals)
                     var.current_value = val
                     results[name] = val
        return results

    def __repr__(self) -> str:
        return f"<SCM '{self.name}': {len(self.variables)} variables>"
