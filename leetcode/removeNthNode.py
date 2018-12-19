# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = head
        end = head

        for current in range(n):
            start = start.next

        if not start:
            return head.next

        while start.next:
            end = end.next
            start = start.next

        end.next = end.next.next

        return head