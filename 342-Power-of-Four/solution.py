class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = bin(num)
        return n.rstrip("0") == "0b1" and len(n[3:]) % 2 == 0