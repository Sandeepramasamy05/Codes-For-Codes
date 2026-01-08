# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        n = len(stack)
        curr = head

        for i in range(n // 2):
            tail = stack.pop()

            nxt = curr.next
            curr.next = tail
            tail.next = nxt

            curr = nxt

        curr.next = None
