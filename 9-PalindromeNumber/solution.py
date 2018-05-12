class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        r = 0
        n = x
        while x > 0:
            r=r*10+x%10
            x = x//10
        return r == n
