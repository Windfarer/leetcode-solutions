class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        for i in s:
            if i in m:
                stack.append(m[i])
            else:
                try:
                    if stack.pop() != i:
                        return False
                except IndexError:
                    return False
        return len(stack) == 0