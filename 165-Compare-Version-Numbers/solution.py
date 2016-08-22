class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        try:
            a = map(int, version1.split("."))
            b = map(int, version2.split("."))
        except ValueError:
            return 0
        l = max(len(a), len(b))
        a.extend([0]*(l-len(a)))
        b.extend([0]*(l-len(b)))
        flag = 0
        for v1, v2 in zip(a, b):
            if v1 > v2:
                flag = 1
                break
            if v1 < v2:
                flag = -1
                break
        return flag