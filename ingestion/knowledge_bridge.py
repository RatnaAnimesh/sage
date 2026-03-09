import sys
import os
import time

# Add project root to sys.path
sys.path.append(os.path.dirname(os.getcwd()))

from sage.memory.atomspace import AtomSpace
from ingestion.semantic_parser import SemanticToCategoricalParser, CausalSieve

def run_great_ingestion_demo():
    print("=== SAGE Phase 9: The Great Ingestion (PoC) ===")
    print("Objective: Scale knowledge breadth while maintaining causal depth.\n")
    
    space = AtomSpace("Wiki_Ingestion")
    parser = SemanticToCategoricalParser(space)
    sieve = CausalSieve(ground_rules=["Physics", "Thermodynamics"])
    
    # Mock 'Internet Knowledge' Stream
    data_stream = [
        "The Earth orbits the Sun.",
        "Water boils at 100 degrees.",
        "A donut is a torus with a hole.",
        "Water freezes at 100 degrees.", # Hallucination / Error
        "The moon is made of green cheese." # Surprise / Hypothesis
    ]
    
    print(f"{'Source Sentence':<40} | {'Surprise (VFE)':<15} | {'Action'}")
    print("-" * 75)
    
    for sentence in data_stream:
        # 1. Evaluate Surprise (Active Fact-Checking)
        surprise = sieve.evaluate_truth(sentence)
        
        # 2. Decide Action based on Surprisingness
        if surprise < 0.1:
            action = "✅ GROUNDED"
            parser.ingest_text(sentence)
        elif surprise < 1.0:
            action = "❓ HYPOTHESIZE"
            parser.ingest_text(sentence)
        else:
            action = "❌ REJECTED"
            
        print(f"{sentence:<40} | {surprise:<15.2f} | {action}")
        time.sleep(0.1)

    print("\n--- Ingestion Statistics ---")
    print(f"Total Sentences Processed: {len(data_stream)}")
    print(f"AtomSpace Result: {space}")

if __name__ == "__main__":
    run_great_ingestion_demo()
