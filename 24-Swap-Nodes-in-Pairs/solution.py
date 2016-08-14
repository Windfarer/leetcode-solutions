# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        x = ListNode("x")
        x.next = head
        p = x
        if head and head.next:
            head = head.next
        while p and p.next and p.next.next:
            self.swap(p)
            p = p.next.next
        return head
    def swap(self, p):
        a = p.next
        b = a.next
        a.next = b.next
        b.next = a
        p.next = b