from typing import List, Dict, Tuple, Optional
from sage.memory.atomspace import AtomSpace, Atom, Link
import math

class CausalPlanner:
    """
    Autonomous planning engine that utilizes grounded affordances and causal models
    to achieve desired physical states in the GAIA environment.
    """
    def __init__(self, atomspace: AtomSpace):
        self.space = atomspace

    def generate_stabilization_plan(self, problem_atom_name: str, support_atom_name: str) -> List[Dict]:
        """
        Creates a plan to move a 'SupportSystem' to stabilize an 'Unstable' object.
        """
        plan = []
        
        # 1. Retrieve Current States
        problem_atom = self.space.get_atom(problem_atom_name)
        support_atom = self.space.get_atom(support_atom_name)
        
        if not problem_atom or not support_atom:
            print(f"[Planner] Error: Could not find Atoms {problem_atom_name} or {support_atom_name}")
            return []

        # In a real SAGE, positions are extracted from the most recent 'PerceptionLink'
        # For this sandbox, we'll assume we can get the 'last_known_pos' from the Atom data
        prob_pos = problem_atom.data.get("last_pos")
        supp_pos = support_atom.data.get("last_pos")
        
        if not prob_pos or not supp_pos:
            return []

        # 2. Reasoning: Calculate Vector
        # We want to move the SupportSystem to the XZ-projection of the Unstable Pillar
        target_x = prob_pos[0]
        target_z = prob_pos[2]
        
        dx = target_x - supp_pos[0]
        dz = target_z - supp_pos[2]
        
        distance = math.sqrt(dx**2 + dz**2)
        
        if distance < 1.0:
            print(f"[Planner] {problem_atom_name} is already supported by {support_atom_name}.")
            return []

        # 3. Action Selection: Apply Impulse
        # SAGE calculates that a 'Mobile' support needs a nudge.
        # Simple heuristic: Impulse = distance * mass_constant
        magnitude = distance * 200000 
        impulse_vec = [ (dx/distance) * magnitude, 0, (dz/distance) * magnitude ]
        
        # Verify Affordance: Does it have 'SupportSystem'?
        links = [l for l in self.space.morphisms if isinstance(l, Link) and l.domain == support_atom]
        affs = [l.codomain.name for l in links if l.type == "AffordanceLink"]
        
        if "SupportSystem" not in affs:
             print(f"[Planner] CAUTION: Attempting to use non-support object {support_atom_name} for stabilization.")

        plan.append({
            "action": "apply_impulse",
            "target_body_id": int(support_atom.data.get("body_id", 0)),
            "impulse": impulse_vec,
            "reason": f"Move {support_atom_name} (Support) to stabilize {problem_atom_name} (Unstable)."
        })
        
        return plan
