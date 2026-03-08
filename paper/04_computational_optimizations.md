# 4. Compressing Causality: Algorithmic Scaling Mechanisms

Translating an explicitly deterministic Structural Causal Model (SCM) from theory to large-scale software introduces critical scaling barriers. Massive, tightly coupled cyclic hypergraphs induce an $O(N!)$ combinatorial explosion during deep counterfactual tree searches—a limitation that historically curtailed classical Symbolic AI scaling in favor of generalized neural optimization. SAGE addresses geometric bottlenecks exclusively through physics-based topological factorizations and categorical abstractions.

## 4.1 The O(1) Causal Broadcasting Theorem

In standard connectionist architectures, updating the relationship between $N$ entities (e.g., verifying a global rule across 100,000 specific atoms) requires $O(N^2)$ attention computations or $O(N)$ sequential iterations. SAGE achieves **Constant-Time ($O(1)$) Propogation** through categorical structural factorization.

### 4.1.1 The Proof of Categorical Addressing
Let $\mathcal{C}$ be the Topos of Sheaves representing the agent's knowledge. Let $R$ be a universal causal rule (a morphism in $\mathcal{C}$) and $\mathcal{I} = \{i_1, i_2, \dots, i_n\}$ be the set of physical instances (atoms) grounded in the Distributed AtomSpace.

**Theorem**: If the AtomSpace utilizes categorical addressing, the complexity of applying rule $R$ to all $i \in \mathcal{I}$ is independent of $n$.

**Proof**:
1.  **Logical Factoring**: SAGE first evaluates the rule $R$ on the abstract object $A \in \mathcal{C}$. This derives a truth-value $\chi_A$ in the Heyting algebra $\Omega$. This is a single computation, $O(1)$.
2.  **Structural Pointer Hash**: In the Distributed AtomSpace, instances $i \in \mathcal{I}$ are not independent duplicates. They are defined as **Natural Transformations** from the abstract object $A$. In the underlying hardware, all instances $i$ share a common **Topological Root**.
3.  **Broadcast**: Propagating the truth-value $\chi_A$ to all instances $i$ is implemented as a single **Tensor Write Mask** on the shared root memory. Because the hardware addressing system maps all $n$ instances to the same categorical pointer, the update is a single atomic operation.
$$ \mathbf{T}_{\mathcal{I}}' = \mathbf{T}_{\mathcal{I}} \otimes \mathbb{1}_{\chi_A} $$
Thus, causal consistency is maintained across million-node populations in **$O(1)$** time, enabling real-time reasoning at planetary scales.

## 4.2 Renormalization Group (RG) Coarse-Graining

Executing counterfactual simulations over granular, high-density topologies generates intractable localized processing noise. Derived from non-equilibrium statistical mechanics, SAGE invokes **Renormalization Group (RG) Coarse-Graining** to manage complexity.

### 4.2.1 The Renormalization Mapping
Let $H(\sigma)$ be the energy (prediction error) of a microscopic causal graph. SAGE introduced a coarse-graining operator $R$ that maps microscopic states $\sigma$ to macroscopic states $\sigma'$. The objective is to preserve the **Partition Function** $Z$ of the system:
$$ Z = \sum_{\sigma} e^{-\beta H(\sigma)} = \sum_{\sigma'} e^{-\beta H'(\sigma')} $$

SAGE identifies **Isomorphic Interaction Cascades**—regions of the AtomSpace where the logic is structurally redundant. By applying the **Kadanoff Block Spin** transformation, SAGE collapses these regions into a single **Macro-Node**.

**Algorithm for Causal Emergence**:
1.  Identify a sub-graph $G_{sub}$ with high internal coupling (bond dimension $\chi$).
2.  Perform a **Singular Value Decomposition (SVD)** on the joint density matrix of $G_{sub}$.
3.  Retain only the top $k$ singular values that contribute to $99\%$ of the predictive variance.
4.  Collapse $G_{sub}$ into a Macro-Node $M$.
5.  Re-map all external morphisms to point to $M$.

This process surgically prunes microscopic "logical noise," ensuring that the agent’s reasoning is always focused on robust, macroscopic causal dependencies.

## 4.3 Matrix Product States and the O(chi^3) Bound

General cyclic graph contraction is #P-complete. SAGE overcomes this by mapping its cognition into a **Matrix Product State (MPS)**—a 1D chain of tensors.

### 4.3.1 The Causal Renormalization Step
By representing the cognitive state as an MPS, a query (e.g., "Will this action lead to state X?") is reduced to a sequential tensor contraction. For an MPS with bond dimension $\chi$, the complexity of local expectation value calculation is:
$$ \text{Complexity} = O(L \cdot d \cdot \chi^3) $$
Where $L$ is the number of causal steps and $d$ is the topological dimension. 

SAGE enforces a **Hard Truncation** on $\chi$. This is the **Causal Renormalization Step**: we intentionally discard "weak" logical entanglements that exceed the available computational budget. This forces the agent to be "decisively efficient"—it ignores complex, low-probability causal loops in favor of the high-probability causal spine. This guarantees that SAGE never enters an infinite computational loop, even when reasoning about circular, recursive physical systems.

## 4.4 Decentralized Belief Propagation in Forney Graphs

To minimize Variational Free Energy without a monolithic "stop-the-world" bottleneck, SAGE is structured as a **Forney Factor Graph (FFG)**. 

In this decentralized architecture, prediction-error signals behave like **Message Packets**. Each node locally calculates its discrepancy $D_{KL}$ and synchronously communicates this to its neighbors. Because the FFG is sparse (due to RG-collapsing), the messages converge to a stable "Topological Equilibrium" near-instantaneously. This matches the decentralized nature of biological cortical columns, ensuring that SAGE's responsiveness is independent of its total knowledge size.
