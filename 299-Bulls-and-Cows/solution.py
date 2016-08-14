class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = 0
        b = 0
        s = []
        g = []
        for x, y in zip(secret, guess):
            if x != y:
                s.append(x)
                g.append(y)
            else:
                a += 1
        for i in g:
            if i in s:
                s.remove(i)
                b += 1
        return "{}A{}B".format(a, b)