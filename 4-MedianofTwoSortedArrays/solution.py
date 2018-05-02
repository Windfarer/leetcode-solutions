class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        c = []
        while True:
            if not nums1:
                c.extend(nums2[::-1])
                break
            if not nums2:
                c.extend(nums1[::-1])
                break
            x, y = nums1[-1], nums2[-1]
            if x > y:
                c.append(nums1.pop())
            else:
                c.append(nums2.pop())
        if len(c)%2 == 0:
            return (c[len(c)//2] + c[len(c)//2-1])/2
        return float(c[len(c)//2])