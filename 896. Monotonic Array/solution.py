class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return True
        p2 = 1
        status = 0 # 0 init  1 asc 2 desc
        for p2 in range(1,len(A)):
            p1 = p2-1
            if status == 0:
                if A[p1] > A[p2]:
                    status = 1
                elif A[p1] < A[p2]:
                    status = 2
            elif status == 2 and A[p1] > A[p2]:
                return False
            elif status == 1 and A[p1] < A[p2]:
                return False
        return True
        
