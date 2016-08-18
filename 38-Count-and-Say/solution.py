class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = "1"
        for i in range(1, n):
            x = self.do(x)
        return x
    def do(self, n):
        x = list(str(n))
        x.insert(0, "0")
        x.append("0")
        rv = []
        count = 0
        for i in range(1, len(x)):
            if x[i] == x[i-1]:
                count += 1
            else:
                rv.extend([count, x[i-1]])
                count = 1
        rv = rv[2:]
        return "".join(map(str,rv))
        
                                