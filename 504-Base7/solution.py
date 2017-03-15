class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbol = "-" if num < 0 else ""
        result = []
        num = abs(num)
        while num != 0:
            x = num % 7
            result.append(str(x))
            num = num // 7
        if len(result) == 0:
            result = ["0"]
        return symbol + "".join(reversed(result))
