# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        x = ListNode("hello")
        x.next = head
        pp = x
        p = head
        while p:
            if p.val == val:
                if head is p:
                    head = head.next
                pp.next = p.next
            else:
                pp = p
            p = p.next
        
        return head
        