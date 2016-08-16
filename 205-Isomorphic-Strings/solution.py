class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i, j in zip(s,t):
            if i not in d and j not in d.values():
                d[i] = j
            elif d.get(i) != j:
                return False
        return True
                
            