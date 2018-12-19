# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        current = start

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        while l1 != None or l2 != None:
            if l1 == None:
                current.next = l2
                l2 = l2.next
            elif l2 == None:
                current.next = l1
                l1 = l1.next
            else:
                if l1.val > l2.val:
                    current.next = l2
                    l2 = l2.next
                else:
                    current.next = l1
                    l1 = l1.next
            current = current.next

        return start.next