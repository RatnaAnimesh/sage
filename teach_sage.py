"""
Teach SAGE Script (Daemon Mode)

This script acts as the "curriculum" for the SAGE prototype.
It feeds explicit academic facts into the agent's knowledge ingestion pipeline.
It then runs a Continuous Active Inference loop in the background, 
simulating the agent "dreaming" and optimizing its Free Energy over time.
"""

from sage.memory.atomspace import AtomSpace
from sage.causality.scm import SCM
from sage.learning.ingestion import KnowledgeIngestor
from sage.inference.active_inference import ActiveInferenceAgent
from sage.agent.core_agent import SOARAgent
import time
import random

print("=== Initiating SAGE Education Pipeline ===")

# 1. Initialize Blank Brain
space = AtomSpace("Global_Knowledge_Web")
world_dag = SCM("World_Environment_DAG")
ingestor = KnowledgeIngestor(atomspace=space, causal_model=world_dag)

# 2. Define the Curriculum (Raw Triplets)
encyclopedia_facts = [
    ("Socrates", "Is_A", "Human", 100, 100),         
    ("Human", "Is_A", "Mortal", 10000, 10000),       
    ("Swan", "Has_Color", "White", 495, 500),        
    ("Gravity", "Causes", "Falling", 1000, 1000),
    ("Heat", "Causes", "Evaporation", 500, 500),
    ("Rain", "Causes", "Wet_Ground", 300, 305)
]

# 3. Ingest Data
ingestor.ingest_triplets(encyclopedia_facts)
print(f"Ingested {len(encyclopedia_facts)} facts. AtomSpace Nodes: {len(space.objects)}")

# 4. Initialize Active Agent Loop
preferences = {"Wet_Ground": 1.0, "Evaporation": 1.0}
active_inf = ActiveInferenceAgent(generative_model=world_dag, homeostatic_goals=preferences)
agent = SOARAgent(name="SAGE_Background_Processor", active_inference_engine=active_inf)

# 5. Continuous Daemon Loop
print("\n=== Entering Autonomous Cognitive Loop ===")
print("SAGE is now running in the background. Press Ctrl+C to terminate.")

tick = 0
try:
    while True:
        tick += 1
        # Simulate semi-random sensory observations from the ingested SCM variables
        obs_heat = random.choice([0, 1])
        obs_rain = random.choice([0, 1])
        
        observations = {"Heat": obs_heat, "Rain": obs_rain}
        
        # Agent perceives and acts
        agent.step(observations)
        
        # Log to show it's "alive"
        if tick % 5 == 0:
            print(f"[Tick {tick}] Free Energy: {active_inf.current_free_energy:.4f} | " 
                  f"Observed: Heat={obs_heat}, Rain={obs_rain} | "
                  f"SCM Size: {len(world_dag.variables)}")
                  
        time.sleep(2.0) # Tick every 2 seconds

except KeyboardInterrupt:
    print("\n[Shutdown] SAGE cognitive loop terminated by user.")
