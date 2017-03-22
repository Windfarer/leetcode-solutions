class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for index, n in enumerate(nums):
            if n not in d:
                d[n] = {index}
            else:
                for i in d[n]:
                    if abs(i - index) <= k:
                        return True
                d[n].add(index)
        return False
