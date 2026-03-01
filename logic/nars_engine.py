"""
NARS Inference Rules for SAGE

Implements the fundamental logical inference rules of Non-Axiomatic Logic (NAL).
These rules dynamically combine the <f, c> truth values of premise statements
without relying on classical pure-axiomatic truth tables.
"""

from sage.logic.nal import NALTruthValue

class NALEngine:
    """
    Executes specific NAL inferences.
    Given two premises, deduces the resulting truth value.
    """
    @staticmethod
    def deduction(t1: NALTruthValue, t2: NALTruthValue) -> NALTruthValue:
        """
        Deduction rule. If S -> M <f1, c1> and M -> P <f2, c2>, 
        what is the truth of S -> P?
        """
        f = t1.f * t2.f
        c = t1.c * t2.c * t1.f * t2.f
        return NALTruthValue(f, c)

    @staticmethod
    def abduction(t1: NALTruthValue, t2: NALTruthValue) -> NALTruthValue:
        """
        Abduction rule. If P -> M <f1, c1> and S -> M <f2, c2>, 
        what is the truth of S -> P?
        """
        f = t2.f
        c = t1.c * t2.c * t1.f * t2.f / (t1.f + t2.f - t1.f * t2.f + 0.0001) # Avoid div 0
        return NALTruthValue(f, c)

    @staticmethod
    def induction(t1: NALTruthValue, t2: NALTruthValue) -> NALTruthValue:
        """
        Induction rule (symmetric to Abduction).
        If M -> S <f1, c1> and M -> P <f2, c2>, what is S -> P?
        """
        return NALEngine.abduction(t2, t1)

    @staticmethod
    def revision(t1: NALTruthValue, t2: NALTruthValue) -> NALTruthValue:
        """
        Revision rule. Combines two separate observations of the identical statement.
        """
        w1_plus = t1.w_plus
        w1_total = t1.w
        
        w2_plus = t2.w_plus
        w2_total = t2.w
        
        w_new_plus = w1_plus + w2_plus
        w_new_total = w1_total + w2_total
        
        if w_new_total == 0:
            return NALTruthValue(0.5, 0.0)
            
        f = w_new_plus / w_new_total
        c = w_new_total / (w_new_total + 1.0) # k=1
        return NALTruthValue(f, c)
