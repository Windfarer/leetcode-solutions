class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        maxlen = max(len(num1), len(num2))+1
        n1 = list(num1.rjust(maxlen, '0'))
        n2 = list(num2.rjust(maxlen, '0'))
        c = 0
        for i, n in enumerate(reversed(n2)):
            x = int(n1[maxlen-1-i]) + int(n) + c
            n1[maxlen-1-i] = str(x%10)
            c = 1 if x > 9 else 0
        return "".join(n1).lstrip("0") or "0"