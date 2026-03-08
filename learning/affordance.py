import math
from typing import List, Tuple, Dict
from sage.memory.atomspace import AtomSpace, Atom, Link
from sage.ontology.category import CNode

class AffordanceLearner:
    """
    Analyzes physical behavior from the GAIA stream to induce affordance-based categories.
    This enables SAGE to understand 'what an object can do' or 'be used for'.
    """
    def __init__(self, atomspace: AtomSpace):
        self.space = atomspace
    
    def learn_affordance(self, atom_name: str, trajectory: List[Tuple[float, float, float]], impulse: Tuple[float, float, float]) -> List[str]:
        """
        Calculates properties based on reaction to an impulse.
        Returns a list of affordance labels.
        """
        affordances = []
        if not trajectory:
            return []

        # 1. Mobility Analysis
        # Delta Velocity vs Impulse
        start_v = 0 # Assume started at rest for simplicity in this sandbox window
        y_coords = [p[1] for p in trajectory]
        dist_moved = math.sqrt(sum((a - b)**2 for a, b in zip(trajectory[0], trajectory[-1])))
        
        impulse_magnitude = math.sqrt(sum(i**2 for i in impulse))
        if impulse_magnitude > 0:
            mobility_index = dist_moved / impulse_magnitude
            if mobility_index > 0.01: # Threshold for 'significant' motion
                affordances.append("Mobile")
            else:
                affordances.append("Stationary")
        
        # 2. Stability Analysis
        # Check variance in Y-Axis (toppling)
        y_variance = sum((y - (sum(y_coords)/len(y_coords)))**2 for y in y_coords) / len(y_coords)
        if y_variance > 5.0: # Significant height change during interaction
            affordances.append("Unstable")
        else:
            affordances.append("Stable")

        # 3. Support Analysis
        # If an object is Stationary and at ground level (Y ~ 0)
        if "Stationary" in affordances and abs(trajectory[-1][1]) < 1.0:
            affordances.append("SupportSystem")

        # Inject into AtomSpace
        atom = self.space.get_atom(atom_name)
        if atom:
            for aff in affordances:
                # Create an InheritanceLink or a PropertyLink
                prop_node = CNode(aff)
                prop_atom = Atom(prop_node.name, prop_node)
                self.space.add_atom(prop_atom)
                
                # Link: GroundedObject -> HasAffordance -> Category
                link_name = f"Link_{atom_name}_{aff}"
                link = Link(link_name, atom, prop_atom, link_type="AffordanceLink")
                self.space.add_link(link)
                
            print(f"[Affordance] {atom_name} induced as: {affordances}")
            
        return affordances
