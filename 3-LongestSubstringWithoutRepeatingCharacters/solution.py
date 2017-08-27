class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p2 = 0
        l = 0
        c = set()
        for i in range(len(s)):
            if s[i] not in c:
                c.add(s[i])
            else:
                if len(c) > l:
                    l = len(c)
                while p2 < i and s[p2] != s[i]:
                    c.discard(s[p2])
                    p2 += 1
                while p2 < i and s[p2] == s[i]:
                    p2 += 1       
        if len(c) > l:
            l = len(c)
        return l
