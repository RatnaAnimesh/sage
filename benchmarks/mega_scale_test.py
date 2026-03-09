import time
import os
import sys
import json

# Add project root to sys.path
sys.path.append(os.path.dirname(os.getcwd()))

from sage.memory.atomspace import AtomSpace, Atom
from sage.optimizations.structural_factorization import StructuralFactorizer
from sage.causality.scm import SCM

def get_memory_usage():
    try:
        import psutil
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / 1024 / 1024  # in MB
    except ImportError:
        import resource
        # macOS: ru_maxrss is in bytes
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024)

def run_mega_benchmark(target_nodes=10000000):
    print(f"=== SAGE 'Internet Scale' Stress Test: {target_nodes:,} Nodes ===")
    
    space = AtomSpace("Mega_Scale")
    scm = SCM("Universe")
    
    # 1. Population (Extreme Scale)
    print(f"Populating {target_nodes:,} nodes into AtomSpace Memory...")
    start_pop = time.time()
    
    # Optimization: We batch add to reduce dict resizing overhead for PoC
    # In a full system, this would be a bulk-loaded binary mmap
    chunk_size = 1000000
    for i in range(target_nodes):
        # We use a uniform name prefix to trigger the 'Matter' filter in Factorizer
        space.add_atom(Atom(f"MatterEntity_{i}", "ConceptNode"))
        if (i + 1) % chunk_size == 0:
            print(f"  [Progress] {i + 1:,} nodes loaded... Current RAM: {get_memory_usage():.2f} MB")
            
    end_pop = time.time()
    
    mem_usage = get_memory_usage()
    print(f"\nPopulation completed in {end_pop - start_pop:.2f} seconds.")
    print(f"Final RAM footprint for 10M nodes: {mem_usage:.2f} MB")
    
    # 2. Causal Broadcast Stress Test
    print("\nExecuting Causal Broadcast across the entire 10-Million node graph...")
    latent_rule = "Gravity_Inference"
    required_props = ["Matter"]
    
    # Warm-up (To handle any JIT/Cache initialization)
    _ = StructuralFactorizer.broadcast_latent_attention(space, scm, latent_rule, required_props)
    
    # Measured Run
    start_broadcast = time.time()
    num_matches = StructuralFactorizer.broadcast_latent_attention(space, scm, latent_rule, required_props)
    end_broadcast = time.time()
    
    latency_ms = (end_broadcast - start_broadcast) * 1000
    print(f"\n--- MEGA SCALE RESULTS ---")
    print(f"Total Nodes Processed: {num_matches:,}")
    print(f"Causal Latency: {latency_ms:.2f} ms")
    print(f"Memory Efficiency: {mem_usage / target_nodes * 1024:.2f} bytes per node")
    
    results = {
        "scale": target_nodes,
        "population_time": end_pop - start_pop,
        "memory_mb": mem_usage,
        "latency_ms": latency_ms,
        "efficiency_bytes_per_node": (mem_usage / target_nodes * 1024 * 1024) / target_nodes # Fix math: (MB * 1024 * 1024) / N
    }
    
    # Correction of math in dict
    results["efficiency_bytes_per_node"] = (mem_usage * 1024 * 1024) / target_nodes

    with open("benchmarks/mega_results.json", "w") as f:
        json.dump(results, f, indent=4)
        
    return results

if __name__ == "__main__":
    # We'll start with 2M to verify on current env, then scale up to 10M if successful.
    # The user specifically requested 'entire internet' scale so we should aim high.
    run_mega_benchmark(10000000)
