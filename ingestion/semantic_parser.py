from typing import List, Tuple, Optional
from sage.memory.atomspace import AtomSpace, Atom, Link
from sage.inference.free_energy import FreeEnergyCalculator

class SemanticToCategoricalParser:
    """
    The 'Great Ingestion' Bridge: Translates Unstructured Text into 
    Categorical Morphisms for the AtomSpace.
    """
    def __init__(self, atomspace: AtomSpace):
        self.atomspace = atomspace
        # Simplified Concept Dictionary (In production, this is a large-scale NER layer)
        self.concept_map = {
            "earth": "Planet_Earth",
            "sun": "Star_Sun",
            "gravity": "Causal_Law_Gravity",
            "water": "Molecular_H2O",
            "boils": "Phase_Transition_Boiling",
            "orbits": "Morphism_Orbital_Motion"
        }

    def extract_triples(self, text: str) -> List[Tuple[str, str, str]]:
        """
        Parses sentences into (Subject, Verb/Link, Object) triples.
        Example: 'The Earth orbits the Sun' -> ('earth', 'orbits', 'sun')
        """
        words = text.lower().replace(".", "").split()
        triples = []
        
        # Simple extraction logic for PoC
        if "orbits" in words:
            try:
                sub = words[words.index("orbits") - 1]
                obj = words[words.index("orbits") + 1]
                triples.append((sub, "orbits", obj))
            except IndexError:
                pass
        
        if "boils" in words:
            try:
                sub = words[words.index("boils") - 1]
                triples.append((sub, "undergoes", "boiling"))
            except IndexError:
                pass

        return triples

    def ingest_text(self, text: str):
        """Processes text and populates the AtomSpace."""
        triples = self.extract_triples(text)
        ingested_count = 0
        
        for sub, rel, obj in triples:
            # Map to grounded concepts
            n1_name = self.concept_map.get(sub, f"Concept_{sub}")
            n2_name = self.concept_map.get(obj, f"Concept_{obj}")
            link_name = f"Inferred_{rel}_{sub}_{obj}"
            
            node1 = Atom(n1_name)
            node2 = Atom(n2_name)
            link = Link(link_name, node1, node2, link_type=rel)
            
            self.atomspace.add_atom(node1)
            self.atomspace.add_atom(node2)
            self.atomspace.add_link(link)
            ingested_count += 1
            
        return ingested_count

class CausalSieve:
    """
    Active Inference Filter: Identifies hallucinations and contradictions
    in incoming knowledge streams using VFE.
    """
    def __init__(self, ground_rules: List[str]):
        self.ground_rules = ground_rules # e.g. ["Gravity makes things fall"]

    def evaluate_truth(self, claim: str) -> float:
        """
        Calculates Variational Free Energy (Surprise) for a new claim.
        'Water freezes at 100C' -> High Surprise (Flagged)
        'Earth orbits Sun' -> Low Surprise (Accepted)
        """
        # Simulated grounding check
        if "orbits" in claim and "earth" in claim and "sun" in claim:
            return 0.01 # Consistent with Physics grounding
        
        if "freezes" in claim and "100" in claim:
            return 5.0 # Contradiction -> High Surprise
            
        return 0.5 # Neutral/New Info
