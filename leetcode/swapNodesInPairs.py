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
        newHead = self.swapPairs(head.next.next)
        nextNode = head.next
        head.next = newHead
        nextNode.next = head

        return nextNode