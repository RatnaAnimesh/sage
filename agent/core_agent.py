"""
Core SAGE Agent (SOAR Architecture)

Integrates the Active Inference loops with SOAR's cognitive architecture.
The agent operates continuously. When Active Inference cannot resolve unexpected
sensory data (an impasse), the agent triggers a substate to perform deliberative
reasoning and "chunks" the result into procedural memory.
"""

from typing import Dict, Any, List
from sage.inference.active_inference import ActiveInferenceAgent
from sage.causality.scm import SCM

class SOARAgent:
    """
    The orchestrating agent combining SOAR cognitive architecture
    with the SAGE Active Inference thermodynamics.
    """
    def __init__(self, name: str, active_inference_engine: ActiveInferenceAgent):
        self.name = name
        self.engine = active_inference_engine
        
        # Procedural Memory: Fast "System 1" Rules
        self.procedural_memory: List[Dict[str, Any]] = []
        
        # Declarative Memory links directly to the engine's SCM/AtomSpace
        self.working_memory: Dict[str, Any] = {}

    def step(self, observations: Dict[str, float]) -> Dict[str, Any]:
        """A single cognitive tick of the agent."""
        
        # Phase 1: Elaboration (Perception)
        self.working_memory = self.engine.perceive(observations)
        
        # Phase 2: Impasse Detection
        # If free energy (surprise) is too high, the reactive procedural rules fail.
        if self.engine.current_free_energy > 5.0:  # Arbitrary threshold for prototype
            return self._handle_impasse(observations)
            
        # Phase 3: Operator Selection (Action)
        # Identify valid actions from procedural memory
        valid_actions = self._get_applicable_actions()
        
        # SAGE uses Koopman SDEs and Tensor Networks natively inside `act`
        selected_action = self.engine.act(valid_actions)
        return selected_action

    def _handle_impasse(self, observations: Dict[str, float]) -> Dict[str, Any]:
        """
        Triggered when standard actions cannot resolve high Free Energy.
        Creates a substate to perform deep, multi-step deliberative reasoning.
        """
        print(f"[{self.name}] Impasse detected! Free Energy: {self.engine.current_free_energy:.2f}. Entering substate.")
        
        # In a full system, this would trigger NARS theorem proving or 
        # Probabilistic Program evaluation over the AtomSpace to find a novel action sequence.
        
        # Mocking finding a solution:
        novel_action = {"action_type": "explore_novel_state", "target": "unknown"}
        
        # Chunking: Commit the successful resolution to procedural memory
        self._chunk_resolution(observations, novel_action)
        
        return novel_action

    def _chunk_resolution(self, situation: Dict[str, float], solution: Dict[str, Any]) -> None:
        """Converts slow deliberative inferences into quick procedural rules."""
        rule = {"condition": situation, "action": solution}
        self.procedural_memory.append(rule)

    def _get_applicable_actions(self) -> List[Dict[str, Any]]:
        """Matches working memory against procedural rules."""
        # Stub for prototype: Returns a default set of actions
        return [
            {"action_type": "move", "direction": "forward"},
            {"action_type": "observe", "target": "environment"}
        ]

