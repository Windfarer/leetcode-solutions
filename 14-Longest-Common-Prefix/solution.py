class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        rv = []
        n = len(strs)
        i = 0
        while True:
            try:
                p = strs[0][i]
            except IndexError:
                return "".join(rv)
            try:
                for j in range(n):
                    cur = strs[j][i]
                    print cur
                    if cur != p:
                        return "".join(rv)
            except IndexError:
                return "".join(rv)
            p = cur
            rv.append(p)
            i = i+1
        
        