class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        ms = []
        for tp in timePoints:
            h, m = map(int, tp.split(":"))
            total_m = h * 60 + m
            ms.append(total_m)
        ms.sort()
        mdiff = ms[0] - ms[-1]
        if mdiff < 0:
            mdiff = mdiff % 1440
        p = ms.pop()
        while ms:
            np = ms.pop()
            dif = p - np
            if dif < mdiff:
                mdiff = dif
            p = np
        return mdiff
