# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = None
        x = None
        while head:
            n = head.next
            x = head
            x.next = tail
            tail = x
            head = n
        return x