import re
pattern = re.compile(r"[^a-zA-Z0-9]")
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = pattern.sub("", s).lower()
        if len(cleaned) == 0 or len(cleaned) == 1:
            return True
        half = len(cleaned) // 2
        return cleaned[:half] == cleaned[-half:][::-1]
        