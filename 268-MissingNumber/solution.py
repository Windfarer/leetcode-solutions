class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = (1+n)*n/2
        for i in nums:
            total -= i
        return total
