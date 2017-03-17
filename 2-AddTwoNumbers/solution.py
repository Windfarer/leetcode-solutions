# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = p = ListNode("x")
        c = 0
        while l1 or l2 or c:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            n = (s + c) % 10
            c = 1 if s + c > 9 else 0
            p.next = ListNode(n)
            p = p.next
        head = head.next
        return head
                 
                
