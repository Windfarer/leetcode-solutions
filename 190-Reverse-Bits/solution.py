class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(bin(n)[2:][::-1].ljust(32, "0"), 2)