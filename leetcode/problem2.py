#!/usr/bin/python

class Solution(object):
    def reverse(self, x):
        is_negative = False
        
        if x < 0:
            is_negative = True
            x *= -1
            
        s = str(x)
        rev = s[::-1]
        
        ans = int(rev)
        
        if  is_negative:
            ans *= -1
            
        if ans < (-2) ** 31 or ans > 2 ** 31 - 1:
            return 0
        
        return ans
