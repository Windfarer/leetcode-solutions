# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        upper = n
        lower = 1
        p = (upper+lower)//2
        while upper > lower:
            if isBadVersion(p):
                upper = p
            else:
                lower = p + 1
            p = (upper+lower)//2
        return p