# SAGE: Symbolic Active Generative Engine

This repository contains the prototype implementation of the **Symbolic Active Generative Engine (SAGE)**, an ambitious, deterministic framework for realizing embodied Artificial General Intelligence (AGI).

Most modern AI (like LLMs or Diffusion models) relies on "Connectionism"—massive, blind statistical curve-fitting via neural networks. While they scale well with data, they suffer from fundamental, unfixable flaws: they hallucinate structurally, they cannot perform multi-step discrete causal reasoning, and they experience catastrophic forgetting.

SAGE abandons this guessing game. Instead, SAGE is built on deterministic mathematics, topological physics, and thermodynamic principles. It constructs an interpretable, explicitly causal model of the world that grounds symbols autonomously, learns physical dynamics in continuous time, and scales using quantum information algorithms.

---

## 1. The Core Philosophy

To achieve true general intelligence, SAGE enforces four absolute mathematical paradigms:
1. **Geometric Symbol Grounding:** SAGE does not rely on human-curated datasets. It uses Algebraic Topology to parse continuous real-world noise (pixels, audio) directly into discrete, logical concepts.
2. **Dynamic Causal Determinism:** Instead of mimicking statistical correlation ($P(Rain|Umbrella)$), SAGE explicitly maps dynamic cause and effect, learning the structural equations of the environment via Operator Theory to ask robust "What if?" questions.
3. **Explicit Engram Memory:** SAGE stores memories exactly as experienced on discrete "tapes" inside an infinite hypergraph, eliminating catastrophic forgetting entirely.
4. **Thermodynamic Autonomy:** SAGE is not a chatbot waiting for a prompt. It is a biological simulator. It acts continuously to minimize its own Variational Free Energy (thermodynamic surprise).

---

## 2. Unstructured Perception: Topology & Category Theory (`sage/ontology` & `sage/learning`)

### 2.1 Grounding Symbols via Persistent Homology
For an AGI to wake up in a chaotic universe, it must autonomously carve discrete objects out of continuous noise. SAGE achieves this via **Topological Data Analysis (TDA)**. 

When SAGE ingests continuous sensory streams, it does not use a neural network to guess bounding boxes. Instead, it maps the input into a mathematical point cloud and applies **Persistent Homology** to track the geometric shape of the data. As the noise forms connected components and cavities that persist across scales, SAGE distills the data into a strict mathematical summary: a **Persistence Barcode**.

### 2.2 The Categorical Imperative
This Persistence Barcode acts as a mathematical bridge into SAGE's mind, which is built on **Category Theory**.
- **Objects** (`CNode`): SAGE takes a grounded Persistence Barcode and formally crystallizes it into a discrete Object Category (e.g., this geometric blob is a "Dog").
- **Morphisms** (`Morphism`): The explicit relationships mapping one Object to another.
- **Functors** ($F$): Using Functors, SAGE maps entire associative maps onto other maps. If SAGE learns the physical structure of "Inside" (a ball in a box), it maps this exact structure to understand the abstract concept of a "Subset" (odd numbers within integers).

Because SAGE's logic operates on Topos Theory, it abandons Boolean True/False in favor of a **Subobject Classifier** ($\Omega$). This allows SAGE to evaluate truth contextually, natively handling the messy nuance of the real world.

---

## 3. Representation & Reasoning (`sage/memory` & `sage/logic`)

### 3.1 The Distributed AtomSpace
Grounded Categories and Morphisms are stored in SAGE's working memory: the **Distributed AtomSpace**. This is an interactive, continuous hypergraph where concepts (`Atoms`) and connections (`Links`) serve as physical points that SAGE manipulates to weave a cohesive world model.

### 3.2 Non-Axiomatic Logic (NAL)
Because the real world features incomplete information, SAGE evaluates all facts using Pei Wang's **Non-Axiomatic Reasoning System (NARS)**. Every logical link possesses a rigorous tuple: `<Frequency, Confidence>`.
- **Frequency ($f$)**: The proportion of positive evidence vs total evidence (e.g., 80% of observed swans are white).
- **Confidence ($c$)**: The objective totality of evidence bounding the belief.
When SAGE combines facts, it updates confidence mathematically (e.g., $c_{new} = c_1 \times c_2 \times f_1 \times f_2$), ensuring a chain of reasoning is strictly bounded by its weakest premise.

---

## 4. Intervention & Physics: The Thermodynamic Loop (`sage/causality` & `sage/inference`)

### 4.1 The Free Energy Principle
SAGE is motivated strictly by Karl Friston’s **Variational Free Energy Principle**. SAGE acts to minimize thermodynamic entropy (prediction error between its internal generative model and its sensory perceptions).
It runs a continuous two-step loop using simultaneous, decentralized message-passing via **Forney Factor Graphs**:
1. **Perceptual Inference:** When SAGE receives sensory input that contradicts its model (Surprise), nodes synchronously pass their prediction errors to their neighbors, updating their matrix beliefs until the system hits thermodynamic equilibrium.
2. **Active Inference:** SAGE predicts future states and takes physical actions that minimize Expected Free Energy (combining risk and ambiguity). 

### 4.2 Dynamic Do-Calculus and Koopman Operators
To minimize future Free Energy, SAGE must simulate cause and effect. SAGE organizes the world into a **Structural Causal Model (SCM)**. However, because the real world is chaotic and non-linear, SAGE cannot rely on static probabilities.

SAGE utilizes **Koopman Operator Theory** to lift continuous, chaotic environmental dynamics into an infinite-dimensional linear array. When SAGE wants to predict a counterfactual ("What happens if I push this switch?"), it uses Judea Pearl's **do-calculus** intervention operator, $do(X=x)$. It propagates this intervention forward sequentially through the linear Koopman matrix. 
If the resulting physical action results in thermodynamic Surprise, SAGE utilizes Stochastic Gradient Descent to continuously overwrite its internal structural equations (SDEs), dynamically discovering the laws of physics over time.

---

## 5. Algorithmic Mastery: Laptop-Scale Compression

Simulating a massive, cyclic hypergraph engine causes combinatorial explosions that crash standard hardware. SAGE leverages three profound mathematical manipulations to compress offline simulation into bounded time on Apple M-Silicon architecture.

### 5.1 Structural Factorization (Categorical MLA)
To solve the "KV-cache" RAM explosion inherent to testing a single rule against 100,000 distinct entities, SAGE simulates DeepSeek's Multi-Head Latent Attention.
It distills the SCM down to a purely abstract Category Theory Morphism (a "Latent Core"). SAGE runs the Do-Calculus intervention exactly once in $O(1)$ time on the abstract core, and uses parallel tensor arrays to broadcast the resulting confidence score into all matching entity Nodes simultaneously.

### 5.2 Tensor Networks & Matrix Product States (MPS)
Deeply cyclic graphs crash standard Monte Carlo Tree Searches. SAGE borrows from quantum information physics by mapping the SCM hypergraph into a **Tensor Network**. Instead of branching infinitely across the map to evaluate a Do-Calculus intervention, SAGE relies on bounded matrix contractions. By specifically structuring the environment into a **Matrix Product State (MPS)**, SAGE aggressively truncates weak mathematical entanglement (Singular Value Decomposition), surgically isolating only the relevant causal pathways and bypassing the $O(N!)$ combinatorial explosion.

### 5.3 Renormalization Group (RG) Coarse-Graining
When SAGE's microscopic physical variables act coherently (e.g., millions of specific "Atoms"), evaluating Do-Calculus across them is computationally wasteful. SAGE utilizes a statistical physics operator to enforce **Causal Emergence**. It mechanically fuses the dense microscopic array into a single macroscopic proxy node (e.g., "Ball"). SAGE intervenes directly on the macroscopic proxy in $O(1)$ time, entirely shielding the engine from microscopic noise unless the macro-prediction fails.

---

## 6. Live Execution & Testing

SAGE is a fully localized engine capable of ingesting vast swaths of data without breaching RAM limits. 

1. **Interactive Causal Shell:** SAGE includes an interactive REPL terminal. The user can manually query the AtomSpace or trigger dynamic Do-Calculus interventions.
   ```bash
   python3 sage_shell.py
   ```
2. **Infinite Data Streaming:** Using `sage_stream.py`, SAGE continuously reaches out to Wikidata APIs, streams unstructured JSON, logically structures the NARS tuple, stores the engram physically to a localized SQLite background database, and triggers manual memory garbage collection, resulting in a continuous memory overhead of ~0 MB.
3. **Hybrid Guided Bootstrapping:** Using `sage_guided_discovery.py`, SAGE proves it can bridge offline abstraction layers. It is seeded with explicit classical physics axioms, and via Epistemic Foraging algorithms and slight human heuristic nudges, autonomously deduces the structural logic governing molecular chemistry.

---

### Repository Organization
- `sage/ontology/` - The maps: Category Theory and Topos Logic.
- `sage/memory/` - The storage: AtomSpace Hypergraph and Engram tapes.
- `sage/logic/` - The deduction: Non-Axiomatic Logic (frequency & confidence).
- `sage/causality/` - The physics: Dynamic Koopman Models and Do-Calculus equations.
- `sage/inference/` - The motivation: Factor Graph Belief Propagation & Free Energy minimization.
- `sage/agent/` - The orchestrator: Putting it all together into an autonomous loop.
- `sage/optimizations/` - The scaling: MPS Tensor Networks, Categorical MLA, and RG Coarse-Graining.
- `sage/learning/` - Grounding & Data: Persistent Homology TDA and Live API Streamers.
- `sage/discovery/` - The curiosity: Epistemic foraging and hybrid discovery routines.
