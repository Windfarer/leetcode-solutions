class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums))[1::2]:
            if nums[i] == nums[i-1]:
                continue
            else:
                return nums[i-1]
        return nums[-1]
                
            