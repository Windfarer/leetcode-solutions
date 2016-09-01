from math import sqrt
class Solution(object):
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = [0,0]+[1]*(max(2,n)-2)
        for i in range(int(sqrt(n))+1):
            if lst[i] == 1:
                k = 2*i
                while k < n:
                    lst[k] = 0
                    k = k + i
        return lst.count(1)
                    
            
            