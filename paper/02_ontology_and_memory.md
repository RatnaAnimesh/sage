# 2. Geometric Ontologies and Explicit Memory: The Structural Foundation

The fundamental failure of connectionist systems is the lack of a stable, discrete ontology. While neural networks can cluster vectors, they cannot ground them in a way that preserves logical identity across varying contexts. SAGE solves this by replacing the "Latent Space" with a formal **Topological Distributed AtomSpace (DAS)**. This section derives the mechanism by which continuous sensory inputs are crystallized into discrete, categorical logic.

## 2.1 The Symbol Grounding Problem and Topological Data Analysis

An autonomous agent must possess the capacity to interpret a noisy, unstructured universe—parsing continuous arrays of sensory stimuli into discrete boundaries. SAGE achieves verifiable symbol grounding via **Topological Data Analysis (TDA)**.

### 2.1.1 Continuous Point Clouds and Vietoris-Rips Filtration
Continuous sensory data streams are interpreted as high-dimensional point clouds $X \subset \mathbb{R}^n$. To extract the "shape" of this data independent of noise or coordinate transformation, SAGE executes a **Vietoris-Rips Filtration** at scale $\epsilon$.

Let $X$ be a finite set of points in a metric space $(M, d)$. The Vietoris-Rips complex $VR_\epsilon(X)$ is the abstract simplicial complex where a subset $\sigma \subseteq X$ is a simplex if the distance between any two of its points is at most $\epsilon$:
$$ VR_\epsilon(X) = \{ \sigma \subset X \mid \forall x,y \in \sigma, d(x,y) \le \epsilon \} $$

### 2.1.2 The Philosophical Synthesis: Plato, Aristotle, and TDA
The Symbol Grounding Problem—how arbitrary symbols acquire physical meaning—is a contemporary framing of the ancient debate between **Platonic Idealism** and **Aristotelian Realism**. 

*   **The Platonic View**: Categories exist as ideal forms, independent of sensory data. GOFAI attempted to implement this via hard-coded ontologies.
*   **The Aristotelian View**: Categories are derived from the structure of the physical world. Connectionism attempts this via statistical clustering.

SAGE provides the mathematical reconciliation of these views through **Persistent Homology**. In SAGE, the "Ideal Form" (the symbol) is the **Limit** of the sensory data's topological filtration. Plato’s "Forms" are not arbitrary; they are the stable Betti numbers $(\beta_0, \beta_1, \dots)$ that survive across infinite scales of observation. Thus, SAGE grounds Aristotle's realism in Plato's mathematical structure, proving that symbols are not "labels" we apply to data, but **Physical Properties** we discover within it.

### 2.1.3 Persistent Homology and Morse Theory
SAGE computes the **Persistent Homology** of this filtration to identify features that birth and death at varying scales. For each dimension $p$, we track the evolution of the $p$-th homology group $H_p$. 

Specifically, we look for the stability of $H_p$ invariants. A feature that persists across a large interval of $\epsilon$ values is considered a "structural reality," while short-lived features are discarded as noise. This is grounded in **Morse Theory**, where the filtration can be seen as a Morse function $f: X \to \mathbb{R}$ on the point cloud. The critical points of this function (births and deaths of cycles) define the topological signature of the object.

**Formal Symbol Grounding**: A symbol in SAGE is defined as a **Persistence Barcode** $B(X)$. This barcode is a coordinate-invariant representation that maps the continuous geometry of the world into a discrete logical identifier. When SAGE encounters a new object, it performs a direct lookup of the topological invariant in its DAS.

## 2.2 Category Theory: The Logic of Relationships

Once symbols are topologically grounded, they are treated as objects in a **Category** $\mathcal{C}$. In SAGE, intelligence is not found in the nodes (symbols), but in the **Morphisms** (relationships) between them.

### 2.2.1 Limits, Pullbacks, and Cognitive Composition
To perform complex reasoning, SAGE utilizes categorical **Limits** and **Colimits**. For instance, the concept of a "Room" is the **Colimit** of the grounded objects $\{Chair, Table, Floor\}$ within a specific topological sheaf.

One of the most powerful operators in SAGE is the **Pullback**, which allows the engine to perform "constrained inference." Given two causal relationships $f: A \to C$ and $g: B \to C$, the pullback $A \times_C B$ represents the unique object that captures the intersection of those causal paths:
$$ A \times_C B = \{ (a, b) \in A \times B \mid f(a) = g(b) \} $$
This allows SAGE to perform "Logical Triangulation"—grounding a new hypothesis by finding the intersection of multiple independent causal observations.

### 2.2.2 The Topos of Sheaves
Traditional symbolic AI treated symbols as global constants. SAGE recognizes that symbols are **Local Sections** of a truth-sheaf. We define a **Site** $(\mathcal{C}, J)$ over the sensory topology. A **Sheaf** $\mathcal{S}$ is a functor that preserves the gluing properties of the world.

**The Gluing Proof**: Consider sub-regions $U$ and $V$. If SAGE grounds a concept in $U$ and a concept in $V$, and their topological signatures overlap on $U \cap V$, the Sheaf axioms guarantee a unique global section—a single persistent identity in the Distributed AtomSpace. This prevents the agent from creating redundant symbols for the same physical entity across different modalities.

## 2.3 The Distributed AtomSpace: Directed Hypergraph Tensors

The storage substrate for these categorical structures is the **Distributed AtomSpace (DAS)**. In the DAS, every grounded icon, category, and morphism is an **Atom**. Unlike neural weights, Atoms are discrete, addressable, and persistent.

### 2.3.1 Atom Types and Morphism Valence
Each Atom possesses an "Arity" (or Valence). A Node (0-arity) represents a grounded entity, while a Link (n-arity) represents a causal or logical relationship bridging $n$ Atoms. Because SAGE allows Links to bridge other Links, we support **Higher-Order Meta-Cognition**.

### 2.3.2 The Molecular Engram: Localized Tensor Addressing
Each Atom $N_i$ in the DAS holds a **Molecular Engram** $\mathbf{T}_i \in \mathbb{R}^{d \times m \times \chi}$, where $d$ is the dimensionality of the TDA invariant, $m$ is the number of active causal morphisms, and $\chi$ is the bond dimension (Section 4.3).

## 2.4 Immunity to Catastrophic Forgetting: SVD Basis Preservation

Catastrophic Forgetting (CF) is the "Achilles' heel" of connectionism. SAGE avoids this by treating memory as a **Non-Interfering Subspace Expansion**. When a fact $\Delta \mathbf{T}$ is added to an engram, SAGE uses **Singular Value Decomposition (SVD)** to project the new information into the **Null Space** of the existing knowledge.

**Derivation of Basis Preservation**:
Let $U_{old}$ be the orthonormal basis of the current engram $\mathbf{T}_{old}$. The update rule is:
1.  Compute the projector into the old basis: $\mathcal{P}_{old} = U_{old}U_{old}^T$.
2.  Compute the new information $\Delta \mathbf{T}$.
3.  Project $\Delta \mathbf{T}$ into the orthogonal complement: $\Delta \mathbf{T}_{clean} = (I - \mathcal{P}_{old}) \Delta \mathbf{T}$.
4.  Update: $\mathbf{T}_{new} = \mathbf{T}_{old} + \Delta \mathbf{T}_{clean}$.

By construction, $\mathcal{P}_{old} \Delta \mathbf{T}_{clean} = 0$. This mathematically guarantees that the new memory does not interfere with previous grounding.
