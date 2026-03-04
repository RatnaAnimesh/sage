# 3. Thermodynamic Inference and Dynamic Causality

To function as a generalized intelligence, an agent must construct rigorous predictions, handle incomplete information, and continuously intervene in the environment. SAGE unifies these operational directives by synthesizing thermodynamic biological modeling with probabilistic, non-axiomatic logic, moving beyond the static sequence prediction characteristic of Large Language Models.

## 3.1 The SAGE Layer: The Operational Tick

Autoregressive models process inference sequentially via an "Attention Block" defined roughly as `LayerNorm(x + MultiHeadAttention(x))`. Because SAGE governs a localized, embodied causality engine, it processes parallel topological data via an explicit, continuous **Operational Tick**.

One discrete inference layer in SAGE executes the following deterministic tensor pipeline:
1. **Perception ($\mathbf{Top}$):** Continuous data matrices $X_t$ are ingested.
2. **Filtration ($VR_\epsilon$):** Topological grounding calculates $H_p$ invariants.
3. **Graph Instantiation ($\mathcal{C}$):** Functor maps surviving invariants via Subobject Classifiers $\Omega$ to create/update explicit Tensor Blocks $\mathbf{T}_i$ in the Distributed AtomSpace.
4. **Thermodynamic Minimization ($\nabla \mathcal{F}$):** Belief Propagation checks if new graph structure $s_t$ induces Prediction Error against historical Engrams.
5. **Action Generation ($\pi$):** Active counterfactuals ($do(x)$) execute via Koopman linear matrices to select physical outputs that minimize expected future entropy $\mathcal{G}(\pi)$.

## 3.2 Non-Axiomatic Reasoning Under Uncertainty

In unstructured physical environments, absolute certainty is unachievable; truth is necessarily bounded by the limited volume of empirical data. SAGE implements Pei Wang’s **Non-Axiomatic Reasoning System (NARS)**, extending propositional logic to assign a fundamental truth-value tuple $\langle f, c \rangle$ to every logical Morphism.

For any given evidential record $w$ containing positive evidence $w^+$, we define:
- **Frequency ($f$)**: The ratio of positive evidence to total evidence, $f = \frac{w^+}{w}$.
- **Confidence ($c$)**: The mapped volume of accumulated evidence stabilizing the empirical distribution, $c = \frac{w}{w + k}$, where $k$ is an epistemic hyperparameter prioritizing evidential scope over transient noise.

Syllogistic inference (e.g., deduction, abduction, induction) operates via stringent constraint maps. For instance, the deduced confidence of a composite relationship strictly obeys a multiplicative limit surface: $c_{deduction} = c_1 \cdot c_2 \cdot f_1 \cdot f_2$. These constraint surfaces mathematically guarantee that generated hypotheses are strictly bounded, unconditionally preventing the unchecked confidence inflation—and corresponding structural hallucination—endemic to autoregressive models.

## 3.3 The Variational Free Energy Principle

SAGE operates not as a static parameterized function simulating responses, but as an autonomous homeostatic system motivated singularly by Karl Friston’s **Variational Free Energy Principle**. SAGE interprets thermodynamic Surprise (or marginal surprise $\mathcal{S}$) identically to Information Theoretic prediction error: the KL-divergence between its internal generative representation $Q(s)$ and its physical sensory perceptions $P(o, s)$.

To minimize the Variational Free Energy theoretical upper bound ($\mathcal{F}$), the inference engine continuously minimizes:

$$ \mathcal{F} = \mathbb{E}_{Q(s)} [\ln Q(s) - \ln P(o, s)] = D_{KL}[Q(s) || P(s|o)] - \ln P(o) $$

When structural dissonance occurs (i.e., observation $o$ contradicts state mapping $s$), SAGE does not initiate unbounded global backpropagation. Instead, it computes the exact marginal discrepancy and applies a localized gradient descent update step strictly isolated to the offending Tensor Block $\mathbf{T}_i$:

$$ \dot{\mathbf{T}}_i = - \kappa \frac{\partial \mathcal{F}}{\partial \mathbf{T}_i} $$

Where $\kappa$ is a deterministic learning rate bounding the structural velocity. 

This thermodynamic minimization runs as a decentralized two-step phase loop:
1. **Perceptual Inference (Model Updating):** SAGE adjusts internal topological arrangements via $\dot{\mathbf{T}}_i$ to map reality, minimizing $D_{KL}$.
2. **Active Inference (World Intervention):** SAGE samples action policies $\pi$ to minimize *Expected Free Energy* ($\mathcal{G}(\pi)$), minimizing future uncertainty while maximizing epistemic value:

$$ \mathcal{G}(\pi) = \sum_{\tau} \mathbb{E}_{Q(o_\tau, s_\tau | \pi)} [\ln Q(s_\tau | \pi) - \ln P(o_\tau, s_\tau)] $$

## 3.4 Dynamic Operator Theory and Continuous Do-Calculus

Standard Active Inference requires predictive causal simulations. SAGE structures physical reality into a generalized **Structural Causal Model (SCM)**, granting the capability for active mathematical intervention via Judea Pearl’s **Do-Calculus** operator, $do(X=x)$.

However, real-time continuous chaotic dynamics dictate intractable probability densities, traditionally restricting Do-Calculus to fixed directed acyclic graphs. SAGE overcomes this computational barrier by lifting nonlinear dynamics into the infinite-dimensional linear space of observables using **Koopman Operator Theory**.

Let the nonlinear environment state dynamic be $\dot{x} = f(x, u)$. We define an invariant observable dictionary $\Psi(x) = [\psi_1(x), \psi_2(x), ... , \psi_N(x)]^T$. SAGE advances this dictionary using a finite-dimensional approximated Koopman matrix $\mathbf{K}$:

$$ \Psi(x_{t+1}) \approx \mathbf{K} \Psi(x_t) + \mathbf{B} u_t $$

Thus, complex spatial interventions $do(u_t)$ bypass $O(N!)$ Monte Carlo physics simulations completely, instead propagating deterministically through a simple linear matrix.

When deterministic consequences diverge from the internal SCM (the Surprise gradient spikes), the topology dynamically leverages **Stochastic Differential Equations (SDEs)** to overwrite the governing interaction laws natively inside the AtomSpace:

$$ dx_t = f(x_t, do(u_t))dt + \sigma(x_t)dW_t $$

By solving this gradient directly, SAGE continuously discovers and formalizes the exact mathematical governing equations of its environment without human proxy or historical language datasets.
