class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        s = sorted(list(enumerate(nums)), key=lambda x: x[1], reverse=True)
        for i, n in enumerate(s):
            if i < 3:
                nums[n[0]] = medals[i]
            else:
                nums[n[0]] = str(i+1)
        return nums
