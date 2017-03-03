class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        r = list(bin(num)[2:])
        for i in xrange(len(r)):
            r[i] = "1" if r[i] == "0" else "0"
        return int("0b{}".format("".join(r)), 2)
