class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return 1
        
        p = 0
        
        while 2 ** (2*(p+1)) <= num:
            p += 1
            
        i = 2**p
        
        while i**2 <= num:
            if i**2 == num:
                return True
            i+=1
            
        return False
