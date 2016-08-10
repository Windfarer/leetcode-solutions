# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pp = ListNode("X")
        p = head
        while p and p.next:
            if p.val == p.next.val:
                pp.next = p.next
                if head is p:
                    head = p.next
            else:
                pp = p
            p = p.next
        return head