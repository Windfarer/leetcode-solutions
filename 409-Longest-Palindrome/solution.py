class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        odd_count = 0
        result = 0
        for k, v in d.items():
            if v % 2 != 0:
                odd_count += 1
            result += v
        if odd_count > 1:
            return result - odd_count + 1
        return result