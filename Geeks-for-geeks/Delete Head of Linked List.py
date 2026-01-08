'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:
    def deleteHead(self, head):
        # code here
        if head is not None:
            head = head.next
        return head
