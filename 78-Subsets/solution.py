class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[n for m, n in zip(format(i, '0{}b'.format(len(nums))), nums) if m == '1'] for i in range(2**len(nums))]
