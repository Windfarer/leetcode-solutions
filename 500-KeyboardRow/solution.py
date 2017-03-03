class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard={
            1:{"q","w","e","r","t","y","u","i","o","p"},
            2:{"a","s","d","f","g","h","j","k","l"},
            3:{"z","x","c","v","b","n","m"}
        }
        rv = []
        for word in words:
            for l in keyboard.values():
                if set(word.lower()).issubset(l):
                    rv.append(word)
        return rv
