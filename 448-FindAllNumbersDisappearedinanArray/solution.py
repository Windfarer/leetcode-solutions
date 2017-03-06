class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*(len(nums)+1)
        for i in nums:
            result[i] = 1
        result = [i for i, n in enumerate(result) if n == 0][1:]
        return result
        
