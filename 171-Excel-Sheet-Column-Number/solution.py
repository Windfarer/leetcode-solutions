class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i, num in enumerate(reversed(s)):
            result += (ord(num)-64) * pow(26, i)
        return result