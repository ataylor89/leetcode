class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        rev = s[::-1]
        
        return s == rev
