"""
Distributed AtomSpace Module for SAGE

Implements a highly scalable, RAM-based hypergraph knowledge representation.
Both declarative data and procedural algorithms are represented as Atoms (Nodes)
and Links (Morphisms) seamlessly coexisting within this geometric space.
"""

import sqlite3
import json
import os
from typing import Dict, List, Optional, Set, Tuple, Union, Any
from sage.ontology.category import Category, CNode, Morphism


class Atom(CNode):
    """
    An Atom in the Distributed AtomSpace. Inherits the categorical properties of a CNode.
    Acts as the base unit of knowledge representation.
    """
    def __init__(self, name: str, atom_type: str = "ConceptNode", data: Any = None):
        super().__init__(name, node_type=atom_type, data=data)


class Link(Morphism):
    """
    A Link connecting Atoms in the AtomSpace. Inherits from categorical Morphism.
    Because SAGE treats links equally, Links themselves can be the domain/codomain of other Links.
    """
    def __init__(self, name: str, domain: Union[Atom, 'Link'], codomain: Union[Atom, 'Link'], link_type: str = "EvaluationLink"):
        # Type ignored for strict categorical typing in python, but conceptually valid in Hypergraphs
        super().__init__(name, domain, codomain, morphism_type=link_type) # type: ignore


class AtomSpace(Category):
    """
    The Hypergraph repository serving as SAGE's working and declarative memory.
    Implements efficient querying over the vast web of conceptual connections.
    """
    def __init__(self, name: str = "Global_AtomSpace", db_path: str = "sage_ltm.db"):
        super().__init__(name)
        # Using Category's self.objects for Atoms and self.morphisms for Links
        
        # Fast-lookup indexes
        self._atoms_by_type: Dict[str, Set[Atom]] = {}
        self._links_by_type: Dict[str, Set[Link]] = {}
        self._name_index: Dict[str, Union[Atom, Link]] = {}
        
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initializes the Long-Term Memory (Disk) table for offloading."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS memory (name TEXT PRIMARY KEY, is_link INTEGER, payload TEXT)')
            conn.commit()

    def add_atom(self, atom: Atom) -> None:
        self.add_object(atom)
        
        if atom.type not in self._atoms_by_type:
            self._atoms_by_type[atom.type] = set()
        self._atoms_by_type[atom.type].add(atom)
        self._name_index[atom.name] = atom

    def add_link(self, link: Link) -> None:
        self.add_morphism(link)
        
        if link.type not in self._links_by_type:
            self._links_by_type[link.type] = set()
        self._links_by_type[link.type].add(link)
        self._name_index[link.name] = link
        
        # Ensure endpoints exist
        if isinstance(link.domain, Atom) and link.domain not in self.objects:
             self.add_atom(link.domain)
        if isinstance(link.codomain, Atom) and link.codomain not in self.objects:
             self.add_atom(link.codomain)

    def get_atom(self, name: str) -> Optional[Atom]:
        element = self._name_index.get(name)
        return element if isinstance(element, Atom) else None

    def query_by_type(self, entity_type: str) -> Set[Union[Atom, Link]]:
        """Retrieve all Atoms or Links of a specific type."""
        res = set()
        if entity_type in self._atoms_by_type:
             res.update(self._atoms_by_type[entity_type])
        if entity_type in self._links_by_type:
             res.update(self._links_by_type[entity_type])
        return res

    def offload_to_disk(self, max_ram_entities: int = 2000) -> int:
        """
        Moves excess Nodes and Links from RAM to the local SQLite database (Long-Term Memory).
        Ensures the agent doesn't crash from OOM during infinite streaming.
        """
        if len(self.objects) <= max_ram_entities:
            return 0
            
        # Select the oldest/first N items to flush to disk
        to_remove_count = len(self.objects) - max_ram_entities
        objects_to_offload = list(self.objects)[:to_remove_count]
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            for obj in objects_to_offload:
                is_link = 1 if isinstance(obj, Link) else 0
                # Simple serialization
                payload = json.dumps({"type": obj.type, "data": str(obj.data)})
                cursor.execute("INSERT OR REPLACE INTO memory VALUES (?, ?, ?)", 
                             (obj.name, is_link, payload))
                
                # Cleanup RAM
                self.objects.discard(obj)
                if isinstance(obj, Link):
                    self.morphisms.discard(obj)
                    if obj.type in self._links_by_type:
                        self._links_by_type[obj.type].discard(obj)
                else:
                    if obj.type in self._atoms_by_type:
                        self._atoms_by_type[obj.type].discard(obj)
                        
                if obj.name in self._name_index:
                    del self._name_index[obj.name]
                    
            conn.commit()
            
        return to_remove_count

    def prune_hypotheses(self, confidence_threshold: float = 0.05) -> int:
        """
        Garbage Collection Optimization for laptop-scale constraints.
        Removes Epistemic Foraging hypotheses that failed Do-Calculus bounds
        repeatedly to free up RAM.
        """
        initial_count = len(self.morphisms)
        links_to_remove = []
        
        for link in self.morphisms:
            val = link.properties.get("truth_value")
            if val and val.c < confidence_threshold:
                 links_to_remove.append(link)
                 
        for link in links_to_remove:
             # Remove from sets
             self.morphisms.remove(link)
             if link.type in self._links_by_type:
                 self._links_by_type[link.type].discard(link)
             if link.name in self._name_index:
                 del self._name_index[link.name]
                 
        return initial_count - len(self.morphisms)

    def __repr__(self) -> str:
        return f"<AtomSpace '{self.name}': {len(self.objects)} Atoms, {len(self.morphisms)} Links>"
