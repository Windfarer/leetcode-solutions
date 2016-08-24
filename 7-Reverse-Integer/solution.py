class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        symbol = 1
        n = str(x)
        if n.startswith("-"):
            symbol = -1
            n = n[1:]
        r = symbol*int("".join(reversed(n)))
        return r if -2147483648 <= r <= 2147483647 else 0