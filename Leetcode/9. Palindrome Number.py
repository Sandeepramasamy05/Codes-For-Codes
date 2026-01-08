class Solution(object):
    def isPalindrome(self, x):
        sum = 0
        tar = x
        while (x > 0):
            digit = x % 10
            sum = (sum*10) + digit
            x = x/10
        if (tar == sum):
            return True
        else:
            return False
