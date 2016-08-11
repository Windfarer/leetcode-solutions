class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
    		return 0
    	if n < 0:
    		x = 1 / x
    		n = -n
    	result = 1
    	while n > 0:
    		if n % 2 == 0:
    			x = x * x
    			n = n // 2
    			continue
    		else:
    			result = result * x
    			n = n - 1
    	return result
        # return pow(x, n)  # just for fun
