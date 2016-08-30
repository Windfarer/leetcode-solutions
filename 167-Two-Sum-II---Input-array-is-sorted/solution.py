class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            if i>0 and numbers[i] == numbers[i-1]:
                continue
            x = target - numbers[i]
            lower = i + 1
            upper = len(numbers)
            while lower < upper:
                p = (lower + upper) // 2
                print p
                if numbers[p] > x:
                    upper = p
                elif numbers[p] < x:
                    lower = p + 1
                else:
                    return [i+1, p+1]
        