'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            
            if s == f:
                return True
        return False
        
        
