import math
class Solution(object):
    def guessNumber(self, n):
        if guess(n) == 0:
            return n
        
        m = n/2
        
        if guess(m) > 0:
  
            while guess(m * 2) > 0:
                m *= 2
            
            while guess(m + int(math.sqrt(m))) > 0:
                m += int(math.sqrt(m))
            
            while guess(m) > 0:
                m += 1
                          
            return m
        
        else:
            while guess(m/2) < 0:
                m /= 2
        
            while guess(m - int(math.sqrt(m))) < 0:
                m -= int(math.sqrt(m))
        
            while guess(m) < 0:
                m -= 1
            
            return m
