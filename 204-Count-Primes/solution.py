from math import sqrt
class Solution(object):
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = [False,False]+[True]*(max(2,n)-2)
        for i in range(int(sqrt(n))+1):
            if lst[i] is True:
                k = 2*i
                while k < n:
                    lst[k] = False
                    k = k + i
        return lst.count(True)
                    
            
            