"""
Teach SAGE Script

This script acts as the "curriculum" for the SAGE prototype.
It feeds explicit academic facts into the agent's knowledge ingestion pipeline.
SAGE translates these facts into its foundational math:
- Category Theory (Objects and Morphisms)
- Hypergraph Memory (AtomSpace)
- Non-Axiomatic Logic (Tuple Truth Values)
- Structural Causal Models (Do-Calculus DAGs)
"""

from sage.memory.atomspace import AtomSpace
from sage.causality.scm import SCM
from sage.learning.ingestion import KnowledgeIngestor
import pprint

print("=== Initiating SAGE Education Pipeline ===")

# 1. Initialize Blank Brain
space = AtomSpace("Global_Knowledge_Web")
world_dag = SCM("World_Environment_DAG")
ingestor = KnowledgeIngestor(atomspace=space, causal_model=world_dag)

# 2. Define the Curriculum (Raw Triplets)
# Format: (Subject, Predicate, Object, Positive_Evidence, Total_Evidence)
encyclopedia_facts = [
    # Biological Taxonomy
    ("Socrates", "Is_A", "Human", 100, 100),         # f=1.0, c=0.99
    ("Human", "Is_A", "Mortal", 10000, 10000),       # f=1.0, c=0.999
    ("Swan", "Has_Color", "White", 495, 500),        # f=0.99, c=0.998 (Black swan problem)
    
    # Physics & Causal Mechanisms
    ("Gravity", "Causes", "Falling", 1000, 1000),
    ("Heat", "Causes", "Evaporation", 500, 500),
    ("Rain", "Causes", "Wet_Ground", 300, 305),
    
    # Intuitionistic Math Concepts (Mapping Functors conceptually)
    ("Circle", "Has_Property", "Round", 10, 10),
    ("Sphere", "Is_3D_Analogue_Of", "Circle", 5, 5)
]

# 3. Ingest Data
ingestor.ingest_triplets(encyclopedia_facts)

# 4. Verification Check
print("\n=== Knowledge Verification ===")
print(f"Total Nodes (Atoms) memorized: {len(space.objects)}")
print(f"Total Edges (Links) memorized: {len(space.morphisms)}")

print("\n[Inspecting NARS Truth Value in AtomSpace]")
swan_link = space.get_atom("Swan_Has_Color_White")
if swan_link:
    print(f"Statement: Swan Has_Color White")
    print(f"Assigned NAL Truth: {swan_link.properties['truth_value']}")

print("\n[Inspecting the Structural Causal Model DAG]")
print(f"Variables mapped explicitly as Causes/Effects: {list(world_dag.variables.keys())}")
print("If SAGE experiences 'Heat', its generative model deterministically expects 'Evaporation'.")

print("\n[Inspecting Discrete Molecular Engram Tape]")
socrates = space.get_atom("Socrates")
if socrates and hasattr(socrates, 'engram'):
    print("Reading exact sequences written to Socrates internal memory:")
    for seq in socrates.engram.sequence:
         print(f" - Timestamp: {seq['timestamp']:.2f} | Fact: {seq['data']}")

print("\nSAGE successfully taught!")
