class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pt = list(pattern)
        sl = str.split()
    
        d = dict()
        if len(pt) != len(sl):
            return False
        for (a, b) in zip(pt, sl):
            if a not in d:
                if b in d.values():
                    return False
                d[a] = b
            elif d[a] != b:
                return False
        return True