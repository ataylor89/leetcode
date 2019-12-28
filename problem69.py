class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        
        if x == 1: 
            return 1
        
        i = 1
        
        while i < int(x/2 + 1):
            if i*i == x:
                return i
            
            if i*i < x and (i+1)*(i+1) > x:
                return i
            
            if i == 1:
                i += 1
                continue
                        
            n = 2
            while i**(n+2) < x:
                n += 2
            
            if n >= 4:
                i = i**(n/2)
            else:
                i += 1
