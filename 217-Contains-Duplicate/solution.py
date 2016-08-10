class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
        # s = set()
        # for i in nums:
        #     if i in s:
        #         return True
        #     s.add(i)
        # return False