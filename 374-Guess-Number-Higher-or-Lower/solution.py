# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.g(0, n)
    
    
    def g(self, low, up):
        guess_num = (low + up+1) // 2
        r = guess(guess_num)
        if r == 0:
            return guess_num
        elif r == -1:
            return self.g(low, guess_num)
        elif r == 1:
            return self.g(guess_num, up)