class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        sym = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: int(x/float(y))}
        lst = []
        while tokens:
            temp = tokens.pop(0)
            if temp in sym:
                lst[-2] = sym.get(temp)(lst[-2], lst[-1])
                del lst[-1]
            else:
                lst.append(int(temp))
        return int(lst[0])