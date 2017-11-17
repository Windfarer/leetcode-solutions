class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in strs:
            t = tuple(sorted(i))
            if t not in d:
                d[t] = [i]
            else:
                d[t].append(i)
        return list(d.values())
        
