class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cons = count = 0
        while nums:
            if nums.pop() == 1:
               count += 1
            else:
              if count > max_cons:
                  max_cons = count
              count = 0
        if count > max_cons:
            max_cons = count
        return max_cons        
