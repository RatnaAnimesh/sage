# 9. Glossary of SAGE Terminology: A Formal Lexicon

This glossary provides rigorous definitions for the core concepts utilized throughout the SAGE manuscript, ensuring semantic clarity for researchers bridging the gap between Category Theory, Topology, and Artificial Intelligence.

## 9.1 Topological and Geometrical Terms

- **Betti Numbers ($\beta_n$):** In the context of SAGE, Betti numbers represent the count of independent $n$-dimensional cycles in a persistent homology filtration. $\beta_0$ tracks connected components (grounded clusters), while $\beta_1$ tracks 1D loops (cyclic causal dependencies).
- **Bottleneck Distance ($d_B$):** The primary metric used by SAGE to calculate the similarity between two grounded icons. It represents the cost of matching one persistence diagram to another, providing a noise-robust measure of conceptual identity.
- **Filtration (Vietoris-Rips):** The process of thickening a sensory point cloud $X$ by spheres of radius $\epsilon$, creating an nested sequence of simplicial complexes. This is the cornerstone of SAGE's symbol grounding mechanism.
- **Persistent Homology:** The study of topological features (simplicial holes) that persist across varying scales of a filtration. In SAGE, persistence is the mathematical definition of "meaning."
- **Simplicial Complex:** A set of simplices (points, lines, triangles, tetrahedra) that serve as the discrete approximation of a continuous physical object in the Distributed AtomSpace.

## 9.2 Categorical and Logical Terms

- **Adjoint Functor:** A pair of functors that stand in a specific relationship representing a "best approximation." In SAGE, the mapping from sensory point clouds to symbolic Topoi is often treated as an adjunction, ensuring maximal informational fidelity.
- **Category ($\mathcal{C}$):** A mathematical collection of Objects (Atoms) and Morphisms (Links). SAGE treats all knowledge as a category where reasoning is equivalent to morphism composition.
- **Colimit:** The categorical generalization of a "Glue" operation. SAGE uses colimits to assemble high-level concepts (e.g., "Architecture") from lower-level parts (e.g., "Pillars" and "Bases").
- **Heyting Algebra ($\Omega$):** The lattice of truth-values used in a Topos. Unlike Boolean logic, Heyting algebra supports intuitionistic values, allowing SAGE to represent "unknown" or "insufficient evidence" as distinct states.
- **Morphism:** A structure-preserving map between two objects. In the Distributed AtomSpace, morphisms represent causal, logical, or temporal relationships.
- **Natural Transformation:** A map between two functors. SAGE uses natural transformations to represent how a concept (e.g., "Rotation") behaves consistently across different grounded instances.
- **Pullback:** A categorical construction that identifies the "intersection" of two logical paths. It is the primary operator for SAGE's constraint-based reasoning.
- **Sheaf $(\mathcal{S})$:** A tool for systematically tracking local data that is consistently attached to the open sets of a topological space. SAGE uses sheaves to ensure that local observations are "glued" into a consistent global identity.
- **Subobject Classifier:** The object in a Topos that classifies subobjects by truth-values. It is the "reasoning organ" that allows SAGE to evaluate the validity of a logical proposition within its internal universe.

## 9.3 Dynamical and Inferential Terms

- **Active Inference:** A framework derived from theoretical biology where an agent acts to minimize its own surprise (Free Energy). In SAGE, this replaces the traditional reward-maximization objective.
- **Bond Dimension ($\chi$):** A parameter in Matrix Product States (MPS) that limits the maximum amount of entanglement (causal coupling) SAGE tracks. $\chi$ is the hard cap on the engine's "reasoning density."
- **Dissipative Structure:** A physical system that maintains order by exporting entropy. SAGE models its AtomSpace as a dissipative structure that organizes itself via the export of prediction errors.
- **Epistemic Foraging:** Action selection driven by curiosity (uncertainty reduction) rather than immediate goal-satisfaction. Mathematically, it is the maximization of the information gain term in Expected Free Energy.
- **Expected Free Energy ($\mathcal{G}$):** The objective function for policy selection in Active Inference. It predicts the surprise of future states, balancing exploration (epistemic) and exploitation (pragmatic).
- **Friston Gradient:** The pathway of steepest descent on the Free Energy manifold. SAGE updates its internal memory (engrams) by following this gradient.
- **Koopman Operator ($\mathcal{K}$):** A linear operator that governs the evolution of scalar observables of a non-linear system. SAGE uses Koopman operators to perform linear causal interventions ($do$-calculus).
- **Matrix Product State (MPS):** A tensor network decomposition used in quantum information theory. SAGE maps its hierarchical graph into an MPS to ensure that inference remains contractible in $O(\chi^3)$ time.
- **Operational Tick:** The unified cognitive loop of SAGE, executing perception, filtration, inference, and action in a single, continuous temporal window.
- **Variational Free Energy ($\mathcal{F}$):** A thermodynamic bound on surprise. SAGE minimizes $\mathcal{F}$ to ensure its internal model remains aligned with external sensory reality.

## 9.4 Hardware and Architecture Terms

- **Distributed AtomSpace (DAS):** High-performance, decentralized knowledge base where every logical unit is an addressable "Atom."
- **Molecular Engram:** The localized tensor block $\mathbf{T}_i$ attached to an Atom, containing the temporal and topological signatures of that symbol.
- **RG-Collapse (Renormalization Group):** The algorithmic process of collapsing redundant microscopic logic into stable macroscopic nodes. This is the primary driver of SAGE's hierarchical scaling.
- **Tensor Processing Unit (TPU-edge):** The target hardware class for SAGE, emphasizing massive parallel tensor contractions over sequential instruction execution.
