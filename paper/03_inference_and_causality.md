# 3. Thermodynamic Inference and Dynamic Causality

Intelligence is not merely the capacity to represent the world, but the capacity to act upon it to minimize surprise. SAGE operationalizes this via **Active Inference**, a framework that unifies perception and action under the umbrella of thermodynamic minimization. This section derives the mathematical core of SAGE's reasoning engine, from the operational tick to the Friston gradient update.

## 3.1 The Variational Free Energy Principle

SAGE operates as a self-organizing system that maintains its structural integrity by minimizing its **Variational Free Energy** ($\mathcal{F}$). According to Karl Friston’s Free Energy Principle, an agent’s surprisal (the negative log-probability of its sensory observations) is upper-bounded by $\mathcal{F}$.

### 3.1.1 The Functional Derivation
Let $s$ be the sensory observations and $\psi$ be the internal hidden states (the Atoms in the DAS). The Free Energy functional $\mathcal{F}(Q, s)$ is defined over a variational distribution $Q(\psi)$ as:
$$ \mathcal{F}(Q, s) = D_{KL}[Q(\psi) \| P(\psi, s)] $$
Expanding this, we get:
$$ \mathcal{F} = \int Q(\psi) \ln \frac{Q(\psi)}{P(\psi, s)} d\psi = \underbrace{D_{KL}[Q(\psi) \| P(\psi)]}_{\text{Complexity}} - \underbrace{\mathbb{E}_Q[\ln P(s | \psi)]}_{\text{Accuracy}} $$

Minimizing $\mathcal{F}$ forces the agent to maximize the accuracy of its models while minimizing their structural complexity (Occam's Razor).

### 3.1.2 The Thermodynamics of Reason: Dissipative Structures

Active Inference in SAGE is not merely an optimization algorithm; it is a physical process of **Dissipative Self-Organization**. Following Nobel laureate Ilya Prigogine, we model the Distributed AtomSpace as a "Dissipative Structure"—a system that maintains its order (low entropy) by exporting entropy to its environment.

**The Entropy Export Proof:**
Let $\Sigma$ be the entropy of the DAS. The rate of change $\dot{\Sigma}$ is decomposed into internal production $d_i \Sigma \ge 0$ and external flow $d_e \Sigma$:
$$ \dot{\Sigma} = d_i \Sigma + d_e \Sigma $$
By minimizing Variational Free Energy $\mathcal{F}$, SAGE ensures that $d_e \Sigma$ is maximized during learning. When SAGE "understands" a new physical law, it is effectively finding a lower-entropy configuration of its internal morphisms. This thermodynamic drive explains why SAGE is inherently "curious": exploring the environment is the only way to find the data required to export internal entropy and maintain structural stability (homeostasis). 

### 3.1.3 The Friston Gradient Update
In SAGE, every Molecular Engram $\mathbf{T}_i$ is treated as a parameter of the variational distribution $Q$. The "Operational Tick" of the system is the localized update of these tensors to follow the descent of the Free Energy manifold:
$$ \dot{\mathbf{T}}_i = - \kappa \nabla_{\mathbf{T}_i} \mathcal{F} $$
Where $\kappa$ is the **Cognitive Flux Rate**.

**Derivation of the Gradient:**
1.  Compute the Prediction Error: $\epsilon = s - \mu(\mathbf{T}_i)$, where $\mu$ is the causal generative model.
2.  Apply the inverse covariance (Precision) matrix $\Pi$: $\bar{\epsilon} = \Pi \epsilon$.
3.  The gradient is the projection of this error back onto the engram's basis via the Koopman operator. This ensures that SAGE's "thoughts" are always driven by a physical need to align its internal state with sensory reality.

## 3.2 Non-Axiomatic Reasoning Under Uncertainty

In unstructured physical environments, absolute certainty is unachievable; truth is necessarily bounded by the limited volume of empirical data. SAGE implements Pei Wang’s **Non-Axiomatic Reasoning System (NARS)**, extending propositional logic to assign a fundamental truth-value tuple $\langle f, c \rangle$ to every logical Morphism.

For any given evidential record $w$ containing positive evidence $w^+$ and negative evidence $w^-$, we define:
- **Frequency ($f$)**: $f = \frac{w^+}{w}$, representing the empirical ratio of successful observations.
- **Confidence ($c$)**: $c = \frac{w}{w + k}$, where $k$ is an epistemic hyperparameter prioritizing evidential scope over transient noise.

SAGE reconciles the "experience-grounded semantics" of NARS with the "model-theoretic" structure of Topos Logic by treating the Topos not as an external absolute model, but as the mathematical universe of the agent's subjective history. In this framework, the Subobject Classifier $\Omega$ becomes a dynamic map of the agent's evidential experience, effectively categoricalizing NARS truth values $\{f, c\}$ into a stable Heyting algebra.

## 3.3 Expected Free Energy and Policy Selection

Action in SAGE is framed as the selection of a **Policy** $\pi$ (a sequence of morphisms) that minimizes the **Expected Free Energy** ($\mathcal{G}$) in the future.

### 3.3.1 Epistemic and Pragmatic Value
The objective function $\mathcal{G}(\pi, \tau)$ for a future time $\tau$ is decomposed into two critical terms:
$$ \mathcal{G}(\pi) \approx \underbrace{\mathbb{E}_{Q(s, \psi | \pi)}[\ln Q(\psi | \pi) - \ln Q(\psi | s, \pi)]}_{\text{Epistemic Value}} - \underbrace{\mathbb{E}_{Q(s, \psi | \pi)}[\ln P(s)]}_{\text{Pragmatic Value}} $$

- **Epistemic Value (Information Gain)**: This drives the agent to perform "Epistemic Foraging"—taking actions that reduce its uncertainty about the world. This is the mathematical root of **Curiosity**.
- **Pragmatic Value (Goal Seeking)**: This drives the agent toward states that match its prior preferences (e.g., structural stability).

## 3.4 The Koopman-Causal Bridge: Linearizing Non-Linear Intervention

Traditional causal models (SCMs) struggle with non-linear dynamical systems. SAGE overcomes this via **Koopman Operator Theory**. The Koopman operator $\mathcal{K}$ is an infinite-dimensional linear operator that governs the evolution of scalar observables of a non-linear system.

### 3.4.1 The Equivalence Theorem
We prove that a structural intervention $do(u)$ on a causal graph is equivalent to an **Intervention Projection** on the Koopman matrix.

Let $x_{t+1} = f(x_t, u_t)$ be a non-linear system. SAGE lifts this into a higher-dimensional space of observables $g(x)$. In this space, the dynamics are linear:
$$ g(x_{t+1}) = \mathcal{K} g(x_t) + \mathcal{B} u_t $$

By representing the Distributed AtomSpace as a Koopman Eigenfunction repository, SAGE can perform **Linear Counterfactuals**. To answer "What happens if I push this pillar?", SAGE does not rotate 3D geometries; it simply applies a linear operator to the relevant engram tensors. This allows for near-instantaneous reasoning over complex physical interactions.

## 3.5 The Operational Tick Algorithm

The cognitive loop of SAGE is encapsulated in the **Operational Tick**, which executes thousands of times per second.

```text
Algorithm: The SAGE Operational Tick
------------------------------------
Loop:
  1. Perception:
     Receive sensory point cloud S.
     Execute TDA Filtration -> Extract Persistent Homology H.
  2. Surprise Detection:
     Calculate Variational Free Energy: F = KL[Q(H) || P(H, S)].
     If F > threshold: Initialize Surprise Signal.
  3. Inference (Friston Gradient):
     Update Engrams: T_i <- T_i - kappa * grad(F).
     Broadcast update across Topos morphisms (O(1)).
  4. Counterfactual Planning:
     For candidate policies pi_j:
       Calculate Expected Free Energy G(pi_j).
     Select pi* = argmin(G).
  5. Action:
     Apply Koopman Intervention: T_actions = K * T_state + B * pi*.
     Execute physical do(u).
End Loop
```

By unifying perception, memory, and action into a single thermodynamic descent, SAGE achieves a level of "Global Coherence" impossible in connectionist architectures, where weights are updated in isolation and planning is an expensive, external search process.
