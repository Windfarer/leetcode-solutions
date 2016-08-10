class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        VL= set(["a","e","i","o","u","A","E","I","O","U"])
        v = []
        for i in range(len(s)):
            if s[i] in VL:
                v.append(s[i])
                s[i] = None
        for i in range(len(s)):
            if s[i] == None:
                s[i] = v.pop()
        return "".join(s)
        