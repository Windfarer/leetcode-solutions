class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = None
        i = 0
        p = k % n
        if not p:
            return
        while i < n-1-p-i:
            tmp = nums[i]
            nums[i] = nums[n-1-p-i]
            nums[n-1-p-i] = tmp
            i += 1
        print nums
        i = 0
        while n-p+i < n-1-i:
            tmp = nums[n-p+i]
            nums[n-p+i] = nums[n-1-i]
            nums[n-1-i] = tmp
            i += 1
        print nums
        i = 0
        while i < n-1-i:
            tmp = nums[i]
            nums[i] = nums[n-1-i]
            nums[n-1-i] = tmp
            i += 1
        print nums