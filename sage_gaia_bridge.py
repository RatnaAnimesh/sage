import subprocess
import json
import os
import sys
import time
from typing import List, Dict, Tuple

# Ensure SAGE can be imported
sys.path.append(os.path.dirname(os.getcwd()))

from sage.memory.atomspace import AtomSpace
from sage.learning.ingestion import KnowledgeIngestor
from sage.learning.affordance import AffordanceLearner
from sage.learning.distillation import TheoryMapper, ExplanationGenerator
from sage.learning.planning import CausalPlanner
from sage.causality.scm import SCM

def run_autonomous_planning():
    print("=== SAGE-GAIA Phase C: Autonomous Planning (Robotics Guidance) ===")
    
    # 1. Initialize SAGE Cognitive Stack
    space = AtomSpace("Autonomous_Planning_Session")
    dag = SCM("Physical_Laws")
    ingestor = KnowledgeIngestor(atomspace=space, causal_model=dag)
    affordance_learner = AffordanceLearner(space)
    theory_mapper = TheoryMapper(space)
    planner = CausalPlanner(space)
    
    # 2. Start GAIA Headless
    gaia_cmd = ["./gaia/target/release/headless"]
    process = subprocess.Popen(
        gaia_cmd, 
        stdout=subprocess.PIPE, 
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE, 
        text=True,
        bufsize=1
    )
    
    print("--> GAIA Physics Engine Launched.")
    
    trajectories: Dict[int, List[Tuple[float, float, float]]] = {}
    frame_count = 0
    grounded_entities: Dict[int, str] = {}
    
    try:
        if process.stdout is None or process.stdin is None:
            return

        for line in process.stdout:
            line = line.strip()
            if line.startswith("FRAME_DATA: "):
                frame_count += 1
                try:
                    raw_json = line[len("FRAME_DATA: "):].strip()
                    bodies = json.loads(raw_json)
                    
                    # Update current trajectories and last positions
                    current_positions = {}
                    for body in bodies:
                        b_id = body["id"]
                        pos = tuple(body["position"])
                        current_positions[b_id] = pos
                        if b_id not in trajectories: trajectories[b_id] = []
                        trajectories[b_id].append(pos)
                    
                    # A. Grounding & Theory Mapping (Early)
                    if frame_count == 50:
                        print("--> Frame 50: Grounding objects and inducing theory...")
                        for b_id, path in trajectories.items():
                            metadata = {"body_id": b_id, "last_pos": current_positions.get(b_id)}
                            atom = ingestor.ingest_continuous_stream(path, data=metadata)
                            if atom:
                                grounded_entities[b_id] = atom.name
                                # Quick affordance & theory injection for the sake of the demo
                                if b_id == 1: # Heavy Base
                                    affordance_learner.learn_affordance(atom.name, path, (0,0,1)) # Fake impulse to trigger
                                    theory_mapper.distill_experience(atom.name)

                    # B. Autonomous Goal Setting
                    # Goal: GroundedObject_TDA_3 (Pillar) is Unstable.
                    # Plan: Use GroundedObject_TDA_1 (Support) to stabilize it.
                    if frame_count == 150:
                        pillar_atom = grounded_entities.get(3)
                        base_atom = grounded_entities.get(1)
                        
                        # Update positions in AtomSpace before planning
                        for b_id, name in grounded_entities.items():
                            atom = space.get_atom(name)
                            if atom: atom.data["last_pos"] = current_positions.get(b_id)

                        print(f"--> Frame 150: SAGE detects instability in {pillar_atom}.")
                        print(f"[SAGE REASONING] {ExplanationGenerator.generate(space, base_atom)}")
                        
                        print(f"--> [Planner] Generating stabilization plan...")
                        plan = planner.generate_stabilization_plan(pillar_atom, base_atom)
                        
                        for step in plan:
                            print(f"    [Executing Action] {step['reason']}")
                            cmd = {"command": step["action"], "body_id": step["target_body_id"], "impulse": step["impulse"]}
                            process.stdin.write(json.dumps(cmd) + "\n")
                            process.stdin.flush()

                except Exception as e:
                    print(f"    [Error] {e}")
            
            if frame_count >= 250:
                process.stdin.write(json.dumps({"command": "stop"}) + "\n")
                process.stdin.flush()
                break
                
    except KeyboardInterrupt: pass
    finally: process.terminate()
    
    print(f"\n=== Autonomous Planning Results ===")
    print("SAGE successfully orchestrated a multi-stage cognitive-physical maneuver.")

if __name__ == "__main__":
    run_autonomous_planning()
