# thanks to great scientist Isaac Newton, but this is not the quickest solution for integer answer
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        g1 = x / 2.0
        while True:
            g2 = (g1 + x/g1) / 2
            if int(g1) == int(g2):
                break
            g1 = g2
        return int(g2)
