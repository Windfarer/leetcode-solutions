class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        for i in range(1,n+1):
            item = ""
            if i % 3 == 0:
                item = "Fizz"
            if i % 5 == 0:
                item += "Buzz"
            if not item:
                item = str(i)
            results.append(item)
        return results
