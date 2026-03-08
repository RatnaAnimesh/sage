from typing import List, Tuple, Optional, Dict
from sage.ontology.category import CNode, Morphism
from sage.memory.atomspace import AtomSpace, Atom, Link
import random
import math

class PointCloud:
    """Represents raw, continuous sensory input in 3D space."""
    def __init__(self, points: List[Tuple[float, float, float]]):
        self.points = points

    def distance(self, p1: Tuple[float, float, float], p2: Tuple[float, float, float]) -> float:
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

class PersistentHomology:
    """
    Computes the Vietoris-Rips filtration over a PointCloud.
    Finds structural equivalence to ground symbols.
    """
    def __init__(self, cloud: PointCloud):
        self.cloud = cloud
    
    def compute_barcode(self, max_epsilon: float = 10.0) -> List[Tuple[int, float, float]]:
        """
        Calculates the persistence of connected components in the sensor stream.
        We look for 'crystallization' - when data points are sufficiently grouped
        to signify a distinct physical object.
        """
        if not self.cloud.points:
            return []
            
        # Simplified Betti-0 persistence:
        # 1. Calculate the 'Spread' of the point cloud.
        # 2. If the points are highly clustered (stable object), persistence is infinite.
        # 3. If they are scattered (random noise), persistence dies quickly.
        
        # Calculate centroid
        n = len(self.cloud.points)
        cx = sum(p[0] for p in self.cloud.points) / n
        cy = sum(p[1] for p in self.cloud.points) / n
        cz = sum(p[2] for p in self.cloud.points) / n
        
        # Calculate variance (stability)
        variance = sum(
            (p[0]-cx)**2 + (p[1]-cy)**2 + (p[2]-cz)**2 
            for p in self.cloud.points
        ) / n
        
        barcode = []
        
        # In this model, if variance < 50.0 (arbitrary), we consider it a 'stable feature'
        # This represents the 'Physical Object' persisting across the sensor stream.
        if variance < 500.0: 
             # We ground a persistent 0-dimensional feature (The Object)
             barcode.append((0, 0.0, float('inf')))
        else:
             # Just thermal/background noise, dies quickly at epsilon related to its spread
             barcode.append((0, 0.0, math.sqrt(variance)))
            
        return barcode

class SymbolGrounder:
    """
    Acts as the Functor between Continuous Data (Topology) and Discrete Logic (AtomSpace).
    """
    def __init__(self, atomspace: AtomSpace):
        self.space = atomspace
        self.grounded_count = 0
        
    def ground_sensor_data(self, raw_sensor_stream: List[Tuple[float, float, float]], data: Optional[Dict] = None) -> Atom:
        """
        Ingests continuous data, computes its topological shape, and injects it 
        as a permanent Category Theory Object if its topological persistence is strong enough.
        """
        if not raw_sensor_stream:
            return None

        cloud = PointCloud(raw_sensor_stream)
        tda = PersistentHomology(cloud)
        
        barcode = tda.compute_barcode()
        
        # Filter for topological features that persist indefinitely
        persistent_features = [feature for feature in barcode if feature[2] == float('inf')]
        
        if not persistent_features:
            return None
            
        self.grounded_count += 1
        symbol_name = f"GroundedObject_TDA_{self.grounded_count}"
        
        # Check if we already grounded a similar object to avoid duplication in this prototype
        # In a real SAGE, we'd use persistent homology distance metrics.
        existing = self.space.get_atom(symbol_name)
        if existing:
            # Update data if provided
            if data:
                existing.data.update(data)
            return existing

        node = CNode(symbol_name)
        new_atom = Atom(node.name, node, data=data)
        
        self.space.add_atom(new_atom)
        print(f"[TDA Grounding] Trajectory crystallized. Generated discrete symbol: {symbol_name}")
        
        return new_atom
