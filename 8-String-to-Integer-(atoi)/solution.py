import re
pattern = re.compile(r"^[+-]{0,1}[0-9]+")
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        r = pattern.search(str.lstrip())
        if r:
            try:
                i = int(r.group(0))
            except ValueError:
                return 0
            return min(max(-2147483648, i), 2147483647)
        return 0