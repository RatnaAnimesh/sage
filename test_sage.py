"""
Integration Test for Symbolic Active Generative Engine (SAGE)

Simulates an agent in a simple environment using the SAGE mathematical constructs:
- It maintains a Structural Causal Model (SCM) of a room's lighting.
- Experiences a sensory prediction error (high Free Energy / "Impasse").
- Triggers the SOAR substate to formulate a do() intervention.
- Utilizes Non-Axiomatic Logic (NAL) to measure truth frequency of its beliefs.
- Saves concepts into the AtomSpace Hypergraph.
"""

from sage.causality.scm import SCM, CausalVariable
from sage.causality.do_calculus import DoCalculus
from sage.inference.active_inference import ActiveInferenceAgent
from sage.agent.core_agent import SOARAgent
from sage.memory.atomspace import AtomSpace, Atom, Link
from sage.logic.nal import create_truth_from_evidence
from sage.logic.nars_engine import NALEngine

print("=== SAGE Initialization ===")

# 1. Setup AtomSpace Memory
space = AtomSpace("Experiment_Space")
print(f"[Memory] Initialized {space}")

# 2. Setup Generative Model (SCM)
env_scm = SCM("Room_Environment")

switch = CausalVariable("Switch", is_exogenous=True)
switch.current_value = 1 # The agent assumes the switch is currently ON.

bulb = CausalVariable("Bulb", is_exogenous=False)
bulb.set_equation(lambda Switch: Switch) # Bulb state equals Switch state

env_scm.add_variable(switch)
env_scm.add_variable(bulb)
env_scm.add_causal_link("Switch", "Bulb")

print(f"[Causality] Generative Model initialized: {env_scm}")

# 3. Active Inference (Preferences)
# Based on the Free Energy Principle, the Agent prefers the light to be ON.
preferences = {"Bulb": 1.0}
active_inf = ActiveInferenceAgent(generative_model=env_scm, homeostatic_goals=preferences)
agent = SOARAgent(name="SAGE_Test_Subject", active_inference_engine=active_inf)

# Mocking the complex internal simulation layer for the prototype test
def mock_simulate(model, action):
    if action["action_type"] == "do":
         cf_model = DoCalculus.intervene(model, action["interventions"])
         outcomes = cf_model.evaluate({})
         # The agent expects that do(Switch=1) guarantees Bulb=1 with 95% probability
         return {"Bulb": 0.95} if outcomes.get("Bulb") == 1 else {"Bulb": 0.05}
    return {}

agent._simulate_action = mock_simulate
agent._get_applicable_actions = lambda: [
    {"action_type": "do", "interventions": {"Switch": 1}, "desc": "Turn switch ON"},
    {"action_type": "do", "interventions": {"Switch": 0}, "desc": "Turn switch OFF"}
]

print("\n=== Cognitive Simulation Step ===")
print("[Perception] Agent observes the room. The sensory input is 'Bulb = 0' (OFF)")
observations = {"Bulb": 0}

action_chosen = agent.step(observations)
print(f"-> Agent's Free Energy (Surprise) after perception: {active_inf.current_free_energy:.2f}")

print("\n[Action] Agent uses Do-Calculus to simulate outcomes and selects lowest Expected Free Energy:")
print(f"-> Selected Action: {action_chosen.get('desc', action_chosen)}")


print("\n=== NARS Logic Verification ===")
# Testing Evidential Reasoning
# Premise 1: S -> M (Switch causes Bulb)
t1 = create_truth_from_evidence(w_plus=4, w_total=5) # 4 successes out of 5
print(f"[Belief 1] Switch causes Bulb: {t1}")

# Premise 2: M -> P (Bulb causes Light)
t2 = create_truth_from_evidence(w_plus=90, w_total=100) # 90 successes out of 100
print(f"[Belief 2] Bulb causes Light: {t2}")

# Inference: S -> P (Switch causes Light)
t3 = NALEngine.deduction(t1, t2)
print(f"[Deduction] Therefore, Switch causes Light: {t3}")

print("\n=== AtomSpace Update ===")
space.add_atom(Atom("Switch"))
space.add_atom(Atom("Light"))
space.add_link(Link("Causes", space.get_atom("Switch"), space.get_atom("Light"), "CausalLink_NAL_Deduction"))
print(f"[Memory] AtomSpace updated: {space}")

print("\nSAGE Integration Test Complete.")
