class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        len_s = len(s)
        p = 0
        for i in g:
            if p >= len_s:
                return count
            while s[p] < i:
                p += 1
                if p >= len_s:
                    return count
            p += 1
            count += 1
        return count
