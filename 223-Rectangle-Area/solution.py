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
        p1 = bool()
        if x<lower and lower<=y<=upper:
            return y - lower
        elif x<lower and y>upper:
            return upper - lower
        elif lower<=x<=upper and lower<=y<=upper:
            return y - x
        elif lower<=x<=upper and y>upper:
            return upper - x
        return 0
        
          