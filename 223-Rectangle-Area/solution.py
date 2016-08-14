class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        return (C-A)*(D-B)+(G-E)*(H-F)-self.get(A,C,E,G)*self.get(B,D,F,H)
        
    def get(self, lower, upper, x, y):
        p1 = bool(x<lower)
        q1 = bool(lower<=x<=upper)
        r1 = bool(x>upper)
        p2 = bool(y<lower)
        q2 = bool(lower<=y<=upper)
        r2 = bool(y>upper)
        if p1 and q2:
            return y - lower
        elif p1 and r2:
            return upper - lower
        elif q1 and q2:
            return y - x
        elif q1 and r2:
            return upper - x
        return 0
        
          