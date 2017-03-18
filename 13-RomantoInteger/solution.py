class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        r = 0
        for i in xrange(len(s)-1):
            if mapping[s[i]] < mapping[s[i+1]]:
                r -= mapping[s[i]]
            else:
                r += mapping[s[i]]
        return r + mapping[s[-1]]
