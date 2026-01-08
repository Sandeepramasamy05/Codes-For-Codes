'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:
    def removeLastNode(self, head):
        # code here

        if head is None:
            return None

        if head.next is None:
            return None

        current = head

        while current.next.next:
            current = current.next

        current.next = None

        return head
