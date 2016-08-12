class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = -1
        try:
            index = haystack.index(needle)
        except ValueError:
            pass
        return index