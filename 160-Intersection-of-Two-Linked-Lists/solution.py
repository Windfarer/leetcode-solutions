# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        while headA:
            headA.seen = True
            headA = headA.next
        while headB:
            if hasattr(headB, "seen"):
                return headB
            headB = headB.next
        return None