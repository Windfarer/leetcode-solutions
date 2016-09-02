class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alpha = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        result = ""
        while n > 0:
            x = n % 26
            result += alpha[x]
            n =( n-(x or 26)) // 26
        return result[::-1]