# The SAGE Architecture Diagram

*(This describes the iconic diagram for the paper, equivalent to the "Encoder/Decoder" block in Attention Is All You Need)*

```mermaid
graph TD
    %% Define Styles
    classDef sensory fill:#f9d0c4,stroke:#e06666,stroke-width:2px;
    classDef ontology fill:#cfe2f3,stroke:#6fa8dc,stroke-width:2px;
    classDef causality fill:#d9ead3,stroke:#93c47d,stroke-width:2px;
    classDef action fill:#fff2cc,stroke:#ffd966,stroke-width:2px;

    %% Abstract Layers
    subgraph "External Mathematical Reality (Continuous)"
        S[Continuous Sensory Data Stream \n e.g. RGB Matrix, Audio]
        A[(Physical Actuator / Output state)]
    end

    subgraph "1. Perceptual Inference (Symbol Grounding)"
        VR["Vietoris-Rips Filtration \n $\epsilon$-scaled mapping"]
        PH["Persistent Homology \n Calculate $H_0, H_1$ Invariants"]
        Functor["Topological Functor \n $\mathcal{F}: \mathbf{Top} \to \mathbf{Set}$"]
    end

    subgraph "2. The Distributed AtomSpace (Geometric Ontology)"
        DAS[("Active Hypergraph Network \n Nodes: Objects \n Edges: Morphisms $g \circ f$")]
        Omega["Topos Subobject Classifier $\Omega$ \n Contextual Truth Boundary"]
    end

    subgraph "3. Active Inference & Do-Calculus"
        Friston{"Variational Free Energy \n Minimize $\mathcal{F}$ Entropy"}
        Koopman["Koopman Operator Linearization \n $d/dt g(x) = \mathcal{K}g(x)$"]
        MPS["Matrix Product State Contraction \n $O(\chi^3)$ Causal Check"]
        Belief["Factor Graph Belief Propagation \n Synchronous Error Gradient"]
    end

    %% Flow Dynamics
    S -->|High-Dimensional \n Point Cloud $X$| VR
    VR --> PH
    PH -->|Survival Barcode| Functor
    Functor -->|Instantiates Discrete \n Categories| DAS

    DAS <-->|Read / Write \n Molecular Engrams| Omega
    DAS -->|Current Topology $s_t$| Friston

    Friston -->|Surprise Detected \n D_KL greater than 0| Koopman
    Koopman -->|Counterfactual Search \n P y bar do x| MPS
    MPS -->|Abstract Abduction| Belief
    Belief -->|Update Matrix| DAS

    Friston -->|Minimize Exp. Free Energy \n G pi| A

    %% Apply Styles
    class S,A sensory;
    class VR,PH,Functor ontology;
    class DAS,Omega causality;
    class Friston,Koopman,MPS,Belief action;
```

## Diagram Caption: 
**Figure 1: The SAGE Architecture.** Continuous environmental data is passed through Vietoris-Rips filtration to derive topological invariants (Persistent Homology). Surviving invariants are mapped via Functor directly into the discrete categorical matrix (Distributed AtomSpace) as explicit Objects and Morphisms, resolving the Symbol Grounding problem without human proxy. Inference evaluates via Forney Factor Graph Message Passing, where Variational Free Energy minimization strictly governs all internal causal adjustments and external physical interventions ($do(x)$). Complex cyclical simulations are linearly compressed via Koopman Operators and bounded spatially via Matrix Product State (MPS) tensor contractions, granting $O(1)$ causal broadcasting capabilities to the global topological manifold limit.
