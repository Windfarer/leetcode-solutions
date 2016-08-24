class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rv = [1]
        for i in range(rowIndex):
            rv = self.next(rv)
        return rv
        
    def next(self, lst):
        lst = [0] + lst + [0]
        rv = []
        for i in range(1,len(lst)):
            rv.append(lst[i-1]+lst[i])
        
        return rv