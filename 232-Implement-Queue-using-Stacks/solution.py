class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        return self.data.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.data[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.data) == 0