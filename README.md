# SAGE: Symbolic Active Generative Engine

This repository contains the prototype implementation of the **Symbolic Active Generative Engine (SAGE)**, an ambitious framework for realizing Artificial General Intelligence (AGI).

To understand SAGE, it helps to first look at what we are *not* doing. Most modern AI (like ChatGPT or Midjourney) relies on "**Connectionism**" (neural networks). Neural networks are essentially giant, blind statistical guessing machines. They take in massive amounts of training data and tweak millions of internal "weights" (connections) until they can reliably guess the next word in a sentence or the next pixel in an image. They don't actually *understand* what they are saying; they just know that the word "apple" statistically appears near the word "red."

SAGE abandons this guessing game completely. Instead of building a statistical mimic, SAGE is built on purely deterministic mathematics, logic, and concepts from biological physics. This document explains the math behind how SAGE actually *thinks*.

---

## 1. The Core Philosophy

Why build SAGE when ChatGPT is already so good? Because neural networks have fatal, unfixable flaws:
1. **They hallucinate:** Because they just guess based on statistics, they confidently lie when they haven't seen enough data.
2. **They have no true memory:** You can't just "tell" a neural network a new fact and have it remember it perfectly forever. It has to be "retrained" on it thousands of times, and doing so often makes it forget older things (catastrophic forgetting).
3. **They don't understand cause and effect:** A neural network might learn that people carrying umbrellas means it's raining ($P(Rain|Umbrella)$), but it might mistakenly think that opening an umbrella *causes* the rain.

SAGE fixes this by demanding:
1. **Mathematical Interpretability:** SAGE uses logic rules, not statistical weights.
2. **Explicit Memory:** SAGE stores memories exactly as written, like saving a file on a hard drive, rather than blurring them into a web of connections.
3. **Causal Determinism:** SAGE explicitly maps out what causes what, allowing it to ask "What if?" questions correctly.
4. **Thermodynamic Autonomy:** Unlike neural networks that have to be constantly fed external data by human supervisors, SAGE is designed to learn autonomously like a biological organism seeking stability.

---

## 2. How SAGE Thinks: Category Theory & Topos Logic (`sage/ontology`)

### 2.1 The Categorical Imperative (Connecting the Dots)
Neural networks turn everything (words, pictures, sounds) into massive lists of numbers (vectors). SAGE turns everything into a mathematical structure called a **Category**.

Think of a Category as a map connecting different concepts.
- The cities on the map are called **Objects** (In code: `CNode`). An Object might be "Socrates" or "Human" or "Mortal."
- The roads connecting the cities are called **Morphisms** (In code: `Morphism`). A Morphism defines the relationship: "Socrates" $\to$[is a]$\to$ "Human."

The magic of Category Theory is **composition**. If you have a road from Object A to Object B, and a road from Object B to Object C, the math *guarantees* you can build a direct road from A to C ($g \circ f: A \to C$). 
- Socrates $\to$ Human
- Human $\to$ Mortal
- *Therefore:* Socrates $\to$ Mortal. SAGE deduces this logical leap instantly without needing thousands of examples to "learn" it.

SAGE can also map entire maps onto other maps using something called a **Functor** ($F$). This is how SAGE does analogies. If it learns the physical structural concept of "Inside" (e.g., a ball is inside a box), it maps that exact same mathematical structure to understand the abstract concept of a "Subset" (e.g., odd numbers are a subset of integers).

### 2.2 Topos Logic (Shades of Gray)
Standard computer logic is Boolean: everything is definitively `True` (1) or `False` (0). But the real world is messy. Is a hotdog a sandwich? True or False?

SAGE uses advanced math called **Topos Theory** to solve this. Instead of a binary True/False, a Topos uses a **Subobject Classifier** ($\Omega$, or "Omega"). 
$\Omega$ acts like an internal translator. When you ask SAGE "Is a hotdog a sandwich?", SAGE uses a mathematical function ($\chi_S : X \to \Omega$) to map the question into $\Omega$. $\Omega$ looks at SAGE's current context and can return dynamic answers like "In the context of ingredients, 80% True. In the context of a restaurant menu, 10% True." SAGE isn't locked into rigid black-and-white thinking.

---

## 3. How SAGE Remembers & Reasons (`sage/memory` & `sage/logic`)

### 3.1 The Distributed AtomSpace
All of these Objects and Morphisms are stored in SAGE's working memory, called the **Distributed AtomSpace**. Imagine it like a giant, interactive 3D spiderweb. Every concept (an `Atom`) and every connection (a `Link`) is a physical point on this web that SAGE can grab and manipulate. SAGE can even create Links that point to other Links, allowing it to think about how it thinks (meta-reasoning).

### 3.2 Non-Axiomatic Logic (NAL)
Because SAGE lives in the real world, it never has perfectly complete information. It uses Pei Wang's **Non-Axiomatic Reasoning System (NARS)**. Whenever SAGE evaluates a fact, it assigns it a tuple: `<Frequency, Confidence>`.

1. **Frequency ($f$)**: Out of all the times I've tested this, how often was it true? Let's say we're testing if swans are white. If SAGE has seen 4 white swans and 1 black swan, the positive evidence ($w^+$) is 4, and the total evidence ($w$) is 5.
  $$ f = \frac{4}{5} = 0.8 $$ (Frequency is 80%)

2. **Confidence ($c$)**: How much total total evidence do I actually have? Seeing 4 white swans out of 5 total swans doesn't mean much compared to seeing 4,000 out of 5,000. Confidence maps the total evidence $w$ bounded between 0 and 1, using a "horizon" constant $k$ (usually just $1$).
  $$ c = \frac{w}{w + 1} $$
  For our 5 swans: $c = \frac{5}{5 + 1} \approx 0.83$ (Confidence is 83%).

When SAGE combines two facts, it updates these numbers mathematically.
**The Deduction Rule:** If SAGE knows Fact 1 (with $f_1, c_1$) and Fact 2 (with $f_2, c_2$), the deduced conclusion has new values:
- New Frequency = $f_1 \times f_2$
- New Confidence = $c_1 \times c_2 \times f_1 \times f_2$

This elegantly ensures that a chain of logic is only as strong as its weakest, least-confident link.

### 3.3 The Intracellular Engram
Neural networks suffer from "catastrophic forgetting" because all memories are mushed together in the network's weights. When it learns a new thing, it slightly overwrites the old things. 

SAGE solves this using the biological theory of the **Engram** (the physical trace of memory). Inside every single `Atom` in the AtomSpace, SAGE has a discrete, addressable "tape" (like a strand of RNA inside a single cell). When SAGE experiences an exact fact or sequence of events, it writes it onto this tape. The memory is perfectly preserved and never decays.

---

## 4. How SAGE Acts: The Thermodynamic Loop (`sage/inference` & `sage/causality`)

### 4.1 The Free Energy Principle
How do we motivate an AGI without a human constantly pressing a "reward" button? SAGE uses the **Free Energy Principle**, a theory by neuroscientist Karl Friston stating that all biological life acts to minimize thermodynamic entropy (disorder/surprise).

SAGE wakes up with "homeostatic preferences" (e.g., "I prefer to have a full battery"). When SAGE predicts the world should look one way, but its sensors tell it something different, it experiences **Surprise** (prediction error). SAGE's ultimate, unyielding goal is to minimize a mathematically calculable upper bound on this surprise, known as **Variational Free Energy ($\mathcal{F}$)**.

The math breaks down into two core objectives:
$$ \mathcal{F} = \text{Complexity} - \text{Accuracy} $$

To minimize $\mathcal{F}$, SAGE runs a continuous two-step loop:
1. **Perceptual Inference (Updating its mind):** SAGE realizes its internal map of the world is wrong, so it changes its internal beliefs to accurately reflect what its sensors are seeing. This makes its world map more accurate.
2. **Active Inference (Changing the world):** SAGE takes physical actions to force the outside world to align with its internal preferences (e.g., walking to a charging station).

### 4.2 Do-Calculus (Understanding Cause & Effect)
To make good decisions, SAGE needs to know *why* things happen. It organizes the world into a **Structural Causal Model (SCM)**—a flowchart of cause and effect.

When SAGE wants to predict the future to minimize Free Energy, it uses Judea Pearl's **do-calculus** intervention operator, written as $do(X=x)$.

If SAGE wants to know "What will happen if I flip the light switch ($X=1$)?", it doesn't just look at past correlations. Instead:
1. It copies its internal SCM flowchart.
2. It mathematically deletes any incoming arrows pointing *to* the Light Switch, because SAGE imposing its will overrides any normal causes for the switch flipping.
3. It forces the Switch variable to $1$ ($x$).
4. It calculates how that change ripples forward through the flowchart equation. $P(y | do(x))$.

This grants SAGE the ability to generate counterfactual universes in its head—safely testing actions mathematically before ever performing them in the real world.

### 4.3 Gödel Optimizer (Safely Getting Smarter)
Because SAGE's own computer code is represented as logic nodes inside its own AtomSpace, SAGE can rewrite its own code to become a better thinker.

However, to prevent SAGE from accidentally breaking itself, it uses a **Gödel Machine** optimizer. Before SAGE changes a single line of code, its internal proof-searcher must mathematically *prove*, using logic theorems, that the new code will be strictly better at lowering Free Energy than the old code. If the proof fails, the modification is immediately rejected. SAGE only gets monotonically smarter.

---
## 5. The Limit of Intelligence (AIXI)
If you combine Category Theory logic, NARS confidence, explicit Engram memory, Do-Calculus, and the Free Energy motivation, what do you get? A computable version of **AIXI**.

AIXI is the theoretical mathematical limit of intelligence formulated by Marcus Hutter. The AIXI equation is:
$$ a_k := \arg\max_{a_k} \sum_{o_k, r_k} \dots \max_{a_m} \sum_{o_m, r_m} [r_k + \dots + r_m] \sum_{p: U(p, a_1\dots a_m) = o_1 r_1 \dots o_m r_m} 2^{-\text{length}(p)} $$

In plain English: AIXI looks at every possible action it could take ($a_k$) across every possible completely simulated universe path ($o, r$) until the end of its lifespan ($m$). It tries to find the action path that provides the maximum possible reward. How does it know which simulated universe is real? It guesses that the simplest mathematical explanation is the most likely to be true ($2^{-\text{length}(p)}$).

Perfect AIXI requires infinite computer power. By substituting infinite search with Active Inference, and infinite universes with Structural Causal Models, SAGE makes reaching the theoretical pinnacle of intelligence achievable.

---
### Repository Organization
- `sage/ontology/` - The maps: Category Theory and Topos Logic.
- `sage/memory/` - The storage: AtomSpace Hypergraph and Engram tapes.
- `sage/logic/` - The deduction: Non-Axiomatic Logic (frequency & confidence).
- `sage/causality/` - The physics: Causal flowcharts and Do-Calculus.
- `sage/inference/` - The motivation: Free Energy minimization formulas.
- `sage/agent/` - The orchestrator: Putting it all together into an autonomous loop.
