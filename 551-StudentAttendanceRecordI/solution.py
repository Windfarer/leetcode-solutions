class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_count = 0
        l_count = 0
        for i in s:
            if i == 'L':
                l_count += 1
            if l_count > 2:
                return False
            if i == 'A':
                a_count += 1
            if i != 'L':
                l_count = 0
            if a_count > 1:
                return False
        return True
