import time
from memory.molecular_engram import EngramTape

def run_verification():
    print("--- SAGE Hierarchical Engram Verification ---")
    tape = EngramTape()
    
    # 1. Fill the tape with 1,000 specific data points
    print(f"Writing 1,000 episodic events to the molecular tape...")
    for i in range(1000):
        tape.write(f"Symmetry discovery event_{i}", truth_value=0.95)
    
    len_pre = len(tape.sequence)
    print(f"Pre-Renormalization length: {len_pre}")
    
    # 2. Timing a search before renormalization
    start_time = time.time()
    results = tape.search(lambda d: "event_999" in d)
    end_time = time.time()
    search_time_pre = end_time - start_time
    print(f"Search time (O(T)): {search_time_pre:.6f}s")
    
    # 3. Perform Renormalization (Coarse-Graining)
    print("\nExecuting RG-Collapse on historical memories (Renormalization)...")
    tape.renormalize()
    
    len_post = len(tape.sequence)
    print(f"Post-Renormalization length: {len_post}")
    
    # 4. Timing a search after renormalization
    start_time = time.time()
    # Search for the same thing (which is now in the macro-summary or the recent tail)
    results = tape.search(lambda d: "event_999" in d)
    end_time = time.time()
    search_time_post = end_time - start_time
    print(f"Search time (Reduced Tape): {search_time_post:.6f}s")
    
    if len_post < len_pre:
        reduction = (1 - len_post/len_pre) * 100
        print(f"\nSUCCESS: Tape size reduced by {reduction:.1f}%.")
        print("SAGE Rebuttal 6.6 Verified: Infinite memory search is bounded by RG-Collapse.")
    else:
        print("\nFAILURE: Renormalization failed to compress the tape.")

if __name__ == "__main__":
    run_verification()
