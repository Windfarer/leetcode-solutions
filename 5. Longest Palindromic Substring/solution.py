class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        result = ""
        for i in range(len(s)):
            tmp = self.check(s, i, i)
            if len(tmp) > len(result):
                result = tmp
            tmp = self.check(s, i, i+1)
            if len(tmp) > len(result):
                result = tmp
        return result
    
    def check(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
