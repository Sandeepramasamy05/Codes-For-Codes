class Solution:
    def searchKey(self, head, key):
        # Code here
        s = head
        while s:

            if s.data == key:
                return True
            s = s.next
        return False
