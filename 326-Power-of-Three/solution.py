class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        x = 3
        while x < n:
            x = x*x
        if x > n:
            while x > n:
                x = x // 3
        return x == n