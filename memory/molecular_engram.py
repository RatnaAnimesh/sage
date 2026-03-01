"""
Intracellular Molecular Engram memory for SAGE

Departing from connectionism, this implements Gallistel's theory of discrete, 
addressable memory sequences inside the nodes themselves. This prevents catastrophic
forgetting by storing exact historical states rather than relying on distributed weights.
"""

from typing import Any, Dict, List, Optional
import time

class EngramTape:
    """
    A discrete, addressable sequence representing facts or history
    stored "inside" a generic computational node.
    Simulates RNA polynucleotide sequence logic.
    """
    def __init__(self):
        # A list of tuples: (timestamp, sequence_data, truth_value)
        self.sequence: List[Dict[str, Any]] = []
        self.head_position: int = 0
        
    def write(self, data: Any, truth_value: float = 1.0) -> int:
        """
        Transcribes a new discrete fact or variable onto the engram tape.
        Returns the address (index) of the newly transcribed sequence.
        """
        entry = {
            "timestamp": time.time(),
            "data": data,
            "truth": truth_value
        }
        self.sequence.append(entry)
        address = len(self.sequence) - 1
        self.head_position = address
        return address

    def read(self, address: int) -> Optional[Dict[str, Any]]:
        """Reads a specific sequence from the molecular tape entirely intact."""
        if 0 <= address < len(self.sequence):
            self.head_position = address
            return self.sequence[address]
        return None

    def search(self, condition: callable) -> List[Dict[str, Any]]:
        """
        Simulates enzymatic pattern matching along the RNA strand.
        Returns all sequences that match the evaluation condition.
        """
        return [seq for seq in self.sequence if condition(seq["data"])]

    def substitute(self, address: int, new_data: Any) -> bool:
        """
        Simulates molecular combinatorial logic where variables are
        deterministically swapped.
        """
        if 0 <= address < len(self.sequence):
             self.sequence[address]["data"] = new_data
             return True
        return False

    def __repr__(self) -> str:
        return f"<EngramTape: {len(self.sequence)} sequences written>"
