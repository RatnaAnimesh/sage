"""
Category Theory Foundations for SAGE

This module implements the foundational categorical constructs for the SAGE architecture.
Rather than using homogeneous tensors, AGI knowledge and algorithms are represented
as morphisms between objects in compositional categories.
"""

from typing import Any, Dict, List, Optional, Protocol, Set, Tuple


class CNode:
    """
    Represents an Object in a mathematical Category (or a Node in a Hypergraph).
    In SAGE, nodes can be conceptual abstractions, sensorimotor states, or logic rules.
    """
    def __init__(self, name: str, node_type: str = "Concept", data: Any = None):
        self.name = name
        self.type = node_type
        self.data = data
        self.properties: Dict[str, Any] = {}

    def __repr__(self) -> str:
        return f"<CNode({self.type}): {self.name}>"

    def __hash__(self) -> int:
        return hash((self.name, self.type))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CNode):
            return False
        return self.name == other.name and self.type == other.type


class Morphism:
    """
    Represents a Morphism (Arrow/Edge) between two Objects in a Category.
    Tracks relationships, structural transitions, or logical implications.
    """
    def __init__(self, name: str, domain: CNode, codomain: CNode, morphism_type: str = "Relation"):
        self.name = name
        self.domain = domain
        self.codomain = codomain
        self.type = morphism_type
        self.properties: Dict[str, Any] = {}

    def __repr__(self) -> str:
        return f"<Morphism({self.type}): {self.domain.name} -> {self.codomain.name}>"

    def compose(self, other: 'Morphism') -> 'Morphism':
        """
        Composition of morphisms (f ∘ g).
        If self is f: A -> B and other is g: B -> C, returns (g ∘ f): A -> C.
        """
        if self.codomain != other.domain:
            raise ValueError(f"Cannot compose {self} with {other}: domain/codomain mismatch.")
        
        comp_name = f"{other.name} ∘ {self.name}"
        comp_type = f"Composition({self.type}, {other.type})"
        return Morphism(comp_name, self.domain, other.codomain, morphism_type=comp_type)

class Category:
    """
    Represents a mathematical Category consisting of Objects (CNodes) and Morphisms.
    Acts as an localized domain of reasoning for the SAGE agent.
    """
    def __init__(self, name: str):
        self.name = name
        self.objects: Set[CNode] = set()
        self.morphisms: Set[Morphism] = set()

    def add_object(self, obj: CNode) -> None:
        self.objects.add(obj)

    def add_morphism(self, morphism: Morphism) -> None:
        if morphism.domain not in self.objects:
            self.objects.add(morphism.domain)
        if morphism.codomain not in self.objects:
            self.objects.add(morphism.codomain)
        self.morphisms.add(morphism)

    def get_morphisms_from(self, obj: CNode) -> List[Morphism]:
        """Returns all outgoing morphisms from an object."""
        return [m for m in self.morphisms if m.domain == obj]

    def get_morphisms_to(self, obj: CNode) -> List[Morphism]:
        """Returns all incoming morphisms to an object."""
        return [m for m in self.morphisms if m.codomain == obj]

    def __repr__(self) -> str:
        return f"<Category: {self.name} | |Ob|={len(self.objects)} |Mor|={len(self.morphisms)}>"


class Functor:
    """
    A mapping from one Category to another that preserves the categorical structure.
    Used for analogical reasoning and translating context between different domains
    within SAGE, e.g., mapping spatial reasoning to linguistic reasoning.
    """
    def __init__(self, name: str, source: Category, target: Category):
        self.name = name
        self.source = source
        self.target = target
        self.object_map: Dict[CNode, CNode] = {}
        self.morphism_map: Dict[Morphism, Morphism] = {}

    def map_object(self, src_obj: CNode, tgt_obj: CNode) -> None:
        if src_obj not in self.source.objects:
            raise ValueError(f"{src_obj} not in source category.")
        self.target.add_object(tgt_obj)
        self.object_map[src_obj] = tgt_obj

    def map_morphism(self, src_morph: Morphism, tgt_morph: Morphism) -> None:
        if src_morph not in self.source.morphisms:
            raise ValueError(f"{src_morph} not in source category.")
        
        # Verify structure preservation
        mapped_domain = self.object_map.get(src_morph.domain)
        mapped_codomain = self.object_map.get(src_morph.codomain)
        
        if tgt_morph.domain != mapped_domain or tgt_morph.codomain != mapped_codomain:
             raise ValueError("Functor must preserve domain and codomain mappings.")

        self.target.add_morphism(tgt_morph)
        self.morphism_map[src_morph] = tgt_morph

    def __repr__(self) -> str:
        return f"<Functor {self.name}: {self.source.name} -> {self.target.name}>"

