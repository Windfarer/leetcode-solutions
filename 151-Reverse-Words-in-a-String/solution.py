class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        lst=s.split()
        lst.reverse()
        return ' '.join(lst)
        