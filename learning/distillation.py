from typing import List, Dict, Tuple, Optional
from sage.memory.atomspace import AtomSpace, Atom, Link
from sage.ontology.category import Category, CNode, Morphism, Functor

class TheoryMapper:
    """
    Acts as the 'Semantic Bridge' between Formal Academic Theory (e.g., Category Theory)
    and Grounded Physical Experiences (e.g., GAIA Affordances).
    """
    def __init__(self, atomspace: AtomSpace):
        self.space = atomspace
        self.theory_category = Category("SAGE_Formal_Theory")
        self.reality_category = Category("GAIA_Experiences")
        
        # Initialize Theory Category with concepts from the SAGE blueprint
        self._init_theory_seeds()

    def _init_theory_seeds(self):
        """Seeds the AtomSpace with high-level cognitive concepts."""
        concepts = [
            ("Topos", "A mathematical universe where logic and geometry coincide."),
            ("Functor", "A map between paradigms that preserves structure."),
            ("Subobject_Classifier", "The mechanism for categorical truth (Truth=1, False=0)."),
            ("Causal_Enforced_Morphism", "A transition grounded in physical law.")
        ]
        for name, desc in concepts:
            atom = Atom(name, atom_type="TheoryNode", data={"description": desc})
            self.space.add_atom(atom)
            self.theory_category.add_object(atom)

    def distill_experience(self, grounded_atom_name: str):
        """
        Attempts to map a physical experience to a theoretical principle.
        E.g., if an object is a 'SupportSystem', it maps to 'Topos_Foundation'.
        """
        grounded_atom = self.space.get_atom(grounded_atom_name)
        if not grounded_atom:
            return

        # Find affordance links
        links = [l for l in self.space.morphisms if isinstance(l, Link) and l.domain == grounded_atom]
        affordances = [l.codomain.name for l in links if l.type == "AffordanceLink"]

        # Mapping Logic (Simplified Cross-Modal Alignment)
        if "SupportSystem" in affordances:
            theory_concept = self.space.get_atom("Topos")
            self._create_distillation_link(grounded_atom, theory_concept, "InstantiationOf")
            print(f"[Distillation] Mapped {grounded_atom_name} (Support) to Theory: 'Topos'")

        if "Mobile" in affordances:
            theory_concept = self.space.get_atom("Functor")
            self._create_distillation_link(grounded_atom, theory_concept, "MorphismMap")
            print(f"[Distillation] Mapped {grounded_atom_name} (Mobile) to Theory: 'Functor' (Spatial Transition)")

    def _create_distillation_link(self, grounded: Atom, theory: Atom, link_type: str):
        link_name = f"Distill_{grounded.name}_{theory.name}"
        link = Link(link_name, grounded, theory, link_type=link_type)
        self.space.add_link(link)

class ExplanationGenerator:
    """
    Generates human-readable (and AI-legible) justifications for SAGE's actions
    by combining theory and grounded experience.
    """
    @staticmethod
    def generate(space: AtomSpace, grounded_atom_name: str) -> str:
        links = [l for l in space.morphisms if isinstance(l, Link) and l.domain.name == grounded_atom_name]
        theory_links = [l for l in links if "Distill" in l.name]
        
        if not theory_links:
            return f"The object {grounded_atom_name} is observed as a physical entity."
            
        theory_node = theory_links[0].codomain
        desc = theory_node.data.get("description", "No description available.")
        
        return f"SAGE identifies {grounded_atom_name} as a physical manifestation of '{theory_node.name}'. " \
               f"In SAGE Theory: {desc}"
