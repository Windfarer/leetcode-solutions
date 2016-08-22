class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i, a in enumerate(s):
            if a not in d:
                d[a] = [i]
            else:
                d[a].append(i)
        r = [i for i in d.values() if len(i) == 1]
        return min(r)[0] if r else -1