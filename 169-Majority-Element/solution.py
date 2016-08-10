class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        length = len(nums) // 2
        for k,v in d.items():
            if v > length:
                return k