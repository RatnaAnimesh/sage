"""
Non-Axiomatic Logic (NAL) implementation for SAGE

Translates Pei Wang's Non-Axiomatic Reasoning System (NARS) truth values.
Truth is not absolute; it is bounded by the Assumption of Insufficient 
Knowledge and Resources (AIKR). Truth is represented as <frequency, confidence>.
"""

import math

class NALTruthValue:
    """
    Experience-grounded semantics.
    Frequency (f): proportion of positive evidence to total evidence.
    Confidence (c): absolute amount of evidence mapped to (0, 1).
    """
    def __init__(self, frequency: float, confidence: float):
        self.f = max(0.0, min(1.0, frequency))
        self.c = max(0.0, min(1.0, confidence))

    @property
    def w(self) -> float:
        """Weight (w): absolute amount of evidence, derived from confidence."""
        if self.c >= 1.0:
            return float('inf')
        return self.c / (1.0 - self.c)

    @property
    def w_plus(self) -> float:
        """Amount of positive evidence."""
        return self.w * self.f

    @property
    def expectation(self) -> float:
        """
        Expected truth value based on current evidence (f) and ignorance (1-c).
        e = c * f + (1 - c) * 0.5
        """
        return self.c * self.f + (1.0 - self.c) * 0.5

    def __repr__(self) -> str:
        return f"<NAL: f={self.f:.3f}, c={self.c:.3f}>"


def create_truth_from_evidence(w_plus: float, w_total: float, k: float = 1.0) -> NALTruthValue:
    """
    Constructs a NAL truth value directly from raw evidence counts.
    k is the horizon parameter (typically 1.0 or 2.0).
    """
    if w_total == 0:
        return NALTruthValue(0.5, 0.0)
    
    f = w_plus / w_total
    c = w_total / (w_total + k)
    return NALTruthValue(f, c)
