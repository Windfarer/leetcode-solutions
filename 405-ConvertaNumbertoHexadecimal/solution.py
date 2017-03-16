class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        r = []
        if num < 0:
            num = 2**32 + num
        while num > 0:
            x = num % 16
            num = num // 16
            r.append(l[x])
        return "".join(reversed(r))
