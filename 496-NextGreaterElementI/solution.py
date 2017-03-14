class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        s = []
        for i in nums:
            while s and s[-1] < i:
                d[s.pop()] = i
            s.append(i)
        return [d.get(i, -1) for i in findNums]
