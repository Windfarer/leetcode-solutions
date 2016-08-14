class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s = list(s)
        r = [[] for i in range(numRows)]
        i = 0
        d = -1
        while s:
            r[i%numRows].append(s.pop(0))
            if i == 0 or i == numRows-1:
                d = -d
            i += d
        return "".join(["".join(i) for i in r])
