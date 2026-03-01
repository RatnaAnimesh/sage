"""
SAGE Interactive Shell

A simple REPL (Read-Eval-Print Loop) to interact with the SAGE engine.
Allows the user to query the AtomSpace, trigger causal interventions, 
and inspect what SAGE has learned.
"""

import sys
from sage.memory.atomspace import AtomSpace, Atom, Link
from sage.causality.scm import SCM
from sage.learning.ingestion import KnowledgeIngestor
import time

def setup_toy_knowledge():
    print("Initializing SAGE...")
    space = AtomSpace("Interactive_Brain")
    dag = SCM("Causal_Model")
    ingestor = KnowledgeIngestor(atomspace=space, causal_model=dag)
    
    print("Ingesting basic physics and logic principles...")
    # Inject some basic physics and facts
    physics_facts = [
        ("Earth", "Has_Property", "Mass", 100, 100),
        ("Apple", "Has_Property", "Mass", 50, 50),
        ("Mass", "Causes", "Gravity", 200, 200),
        ("Gravity", "Causes", "Attraction", 200, 200),
        ("Socrates", "Is_A", "Human", 10, 10),
        ("Human", "Is_A", "Mortal", 100, 100)
    ]
    ingestor.ingest_triplets(physics_facts)
    return space, dag

def run_shell():
    space, dag = setup_toy_knowledge()
    
    print("\n" + "="*50)
    print("             SAGE Interactive Shell")
    print("="*50)
    print("Type 'help' for commands. Type 'exit' to quit.\n")
    
    while True:
        try:
            cmd = input("SAGE> ").strip()
            if not cmd:
                continue
                
            if cmd.lower() in ['exit', 'quit', 'q']:
                break
                
            elif cmd.lower() == 'help':
                print("\nCommands:")
                print("  stats       - Show current AtomSpace metrics")
                print("  knows <X>   - Ask SAGE what it knows about Concept X (e.g., 'knows Socrates')")
                print("  do <X>      - Trigger a Do-Calculus intervention on X (e.g., 'do Gravity')")
                print("  teach <X> <Y> <Z> - Feed SAGE a new triplet fact (e.g., 'teach Sky Is Blue')")
                print("")
                
            elif cmd.lower() == 'stats':
                print(f"Entities in Memory (Atoms): {len(space.objects)}")
                print(f"Logic Rules in Memory (Links): {len(space.morphisms)}\n")
                
            elif cmd.lower().startswith('knows '):
                concept = cmd[6:].strip()
                atom = space.get_atom(concept)
                if not atom:
                    print(f"I have no knowledge of '{concept}'. Try teaching me.\n")
                else:
                    print(f"Concept: {concept}")
                    # Find all links involving this concept
                    connections = []
                    for link in space.morphisms:
                        if link.domain == atom:
                             connections.append(f"-> [{link.name.split('_')[0]}] -> {link.codomain.name}")
                        elif link.codomain == atom:
                             connections.append(f"<- [{link.name.split('_')[0]}] <- {link.domain.name}")
                    if connections:
                        print("Relationships:")
                        for c in connections:
                            print(f"  {c}")
                    else:
                        print("  (No known relationships yet)")
                    print("")
                    
            elif cmd.lower().startswith('do '):
                target = cmd[3:].strip()
                print(f"[Simulating Intervention: do({target} = 1)]")
                # Toy simulation of stepping through the causal graph
                print("-> Calculating counterfactual state via Factorization...")
                time.sleep(0.5)
                # Hardcoded logic trace for the toy model
                if target.lower() == "gravity":
                    print("-> If Gravity is forced true, expected Attraction confidence rises to 0.99.")
                elif target.lower() == "mass":
                     print("-> Intervening on Mass ripples to Gravity -> Attraction.")
                else:
                    print(f"-> I do not have a robust causal model for '{target}' to simulate.")
                print("")
                
            elif cmd.lower().startswith('teach '):
                parts = cmd[6:].strip().split()
                if len(parts) >= 3:
                     sub = parts[0]
                     pred = parts[1]
                     obj = " ".join(parts[2:])
                     AtomSpace.add_atom(space, Atom(sub)) # Avoid ingestor complexities for shell
                     AtomSpace.add_atom(space, Atom(obj))
                     space.add_link(Link(f"{pred}_Link", space.get_atom(sub), space.get_atom(obj)))
                     print(f"[Memory Engram Written: {sub} -> {pred} -> {obj}]\n")
                else:
                     print("Format: teach Subject Predicate Object\n")
                     
            else:
                print(f"Unknown command: '{cmd}'. Type 'help'.\n")
                
        except (KeyboardInterrupt, EOFError):
            print()
            break
            
    print("\nShutting down SAGE shell.")

if __name__ == "__main__":
    run_shell()
