class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = s.split()
        n = len(string)
        
        return len(string[n-1])
            