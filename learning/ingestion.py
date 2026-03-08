"""
Knowledge Ingestion Pipeline for SAGE

Translates structured logical facts (triplets) or natural language into
the strict categorical ontology required by SAGE.
Auto-populates the Distributed AtomSpace and assigns NARS truth values.
"""

from typing import List, Tuple, Optional, Dict, Any
from sage.memory.atomspace import AtomSpace, Atom, Link
from sage.logic.nal import NALTruthValue, create_truth_from_evidence
from sage.causality.scm import SCM, CausalVariable
from sage.learning.persistent_homology import SymbolGrounder

class KnowledgeIngestor:
    """
    Parses facts into SAGE's foundational mathematical data structures.
    """
    def __init__(self, atomspace: AtomSpace, causal_model: Optional[SCM] = None):
        self.space = atomspace
        self.scm = causal_model
        self.symbol_grounder = SymbolGrounder(atomspace)
        
    def ingest_continuous_stream(self, raw_sensor_stream: List[Tuple[float, float, float]], data: Optional[Dict] = None) -> Atom:
        """
        Phase 15 Geometric Symbol Grounding.
        Ingests continuous data directly. Converts pixel arrays into discrete logic
        Atoms autonomously via Topological Persistent Homology.
        """
        print(f"[Ingestor] Received continuous data array. Attempting TDA geometric crystallization...")
        discrete_atom = self.symbol_grounder.ground_sensor_data(raw_sensor_stream, data=data)
        return discrete_atom

    def ingest_triplets(self, facts: List[Tuple[str, str, str, float, float]]) -> None:
        """
        Ingests a list of triplet facts into the AtomSpace.
        Format: (Subject, Predicate, Object, w_plus (successes), w_total (attempts))
        """
        print(f"[Ingestor] Processing {len(facts)} facts into AtomSpace...")
        
        for subj_name, pred_name, obj_name, w_plus, w_total in facts:
            # 1. Resolve or Create Atoms (Categories/Objects)
            subj_atom = self.space.get_atom(subj_name)
            if not subj_atom:
                subj_atom = Atom(subj_name, atom_type="ConceptNode")
                self.space.add_atom(subj_atom)
                
            obj_atom = self.space.get_atom(obj_name)
            if not obj_atom:
                obj_atom = Atom(obj_name, atom_type="ConceptNode")
                self.space.add_atom(obj_atom)
                
            # 2. Create the Link (Categorical Morphism)
            link_name = f"{subj_name}_{pred_name}_{obj_name}"
            # Check if link already exists to avoid redundant edges, though Hyperon allows multigraphs
            existing_link = self.space.get_atom(link_name) # Links are also in the name index in AtomSpace
            
            if not existing_link:
                 link = Link(link_name, domain=subj_atom, codomain=obj_atom, link_type=pred_name)
                 
                 # 3. Assign NARS Truth Value to the Morphism
                 truth = create_truth_from_evidence(w_plus, w_total)
                 link.properties["truth_value"] = truth
                 
                 # 4. Save to AtomSpace
                 self.space.add_link(link)
                 
                 # 5. Write exact explicit memory to EngramTape (prevents catastrophic forgetting)
                 # We write to the Subject's internal tape
                 if not hasattr(subj_atom, 'engram'):
                     from sage.memory.molecular_engram import EngramTape
                     subj_atom.engram = EngramTape()
                 subj_atom.engram.write({
                     "predicate": pred_name, 
                     "target": obj_name, 
                     "nal_truth": truth
                 })
                 
            # 6. Auto-populate SCM if the predicate is causal
            if self.scm and pred_name.lower() in ["causes", "leads_to", "creates"]:
                 self._register_causal_link(subj_name, obj_name)

    def _register_causal_link(self, cause_name: str, effect_name: str) -> None:
        """
        Translates a declarative fact into a Structural Causal Model (DAG) equation.
        """
        if cause_name not in self.scm.variables:
            self.scm.add_variable(CausalVariable(cause_name))
        if effect_name not in self.scm.variables:
             self.scm.add_variable(CausalVariable(effect_name))
             
        # Add the directed edge
        self.scm.add_causal_link(cause_name, effect_name)
        
        # Setup a basic deterministic structural equation for the prototype
        # "If cause is True, effect is True"
        effect_var = self.scm.variables[effect_name]
        
        def structural_eq(**kwargs):
             return kwargs.get(cause_name, 0)
             
        effect_var.set_equation(structural_eq)
        print(f"[Ingestor] Registered Layer 2 Causal Mechanism: {cause_name} -> {effect_name}")
