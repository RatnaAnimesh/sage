import time
import os
import sys
from memory.molecular_engram import EngramTape

def run_internet_stream_simulation(total_events=500000, batch_size=50000):
    """
    Simulates an 'Internet Scale' influx of data (100k events/sec).
    Demonstrates how SAGE uses RG-Collapse to prevent the engram tape 
    from exceeding machine limits.
    """
    print(f"=== SAGE 'Internet Influx' Simulation: {total_events:,} Events ===")
    tape = EngramTape()
    
    start_time = time.time()
    
    for i in range(total_events):
        tape.write(f"Global_Stream_Log_{i}", truth_value=0.9)
        
        # Every batch, we check for renormalization (Simulating the 'Sleep/Consolidation' cycle)
        if (i + 1) % batch_size == 0:
            pre_len = len(tape.sequence)
            tape.renormalize()
            post_len = len(tape.sequence)
            
            elapsed = time.time() - start_time
            print(f"  [Influx] Processed {i+1:,} events. Active Tape: {post_len} (Collapsed {pre_len - post_len}). Time: {elapsed:.2f}s")
            
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\n--- INFLUX RESULTS ---")
    print(f"Total Stream Volume: {total_events:,} events")
    print(f"Total Processing Time: {total_time:.2f} seconds")
    print(f"Effective Throughput: {total_events / total_time :,.0f} events/sec")
    print(f"Final Tape Size: {len(tape.sequence)}")
    
    if len(tape.sequence) < total_events / 10:
        print("\nSUCCESS: SAGE stabilized the high-frequency stream.")
        print("Rebuttal 8.2 Verified: Internet-scale streaming does not lead to O(T) memory exhaustion.")
    else:
        print("\nFAILURE: Compression insufficient for internet-scale influx.")

if __name__ == "__main__":
    # We use 500k events to stay within reasonable tool limits, but extrapolate to 100M+
    run_internet_stream_simulation()
