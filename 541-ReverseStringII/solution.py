class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = len(s)
        p = 0
        result = ""
        while 2*k*p < l:
            result += s[2*k*p:2*k*p+k][::-1] + s[2*k*p+k:2*k*p+2*k]
            p += 1
        return result
