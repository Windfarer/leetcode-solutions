class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        r = [[1]]
        p = [1]
        for i in range(1, numRows):
            n = self.next_line(p)
            r.append(n)
            p = n
        return r
        
        
    def next_line(self, p):
        l = [1]
        for i in range(1,len(p)):
            l.append(p[i-1]+p[i])
        l.append(1)
        return l