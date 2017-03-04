from math import sqrt
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        x = int(sqrt(area))
        while area % x != 0:
            x -= 1
        return [area/x, x]
