class Solution(object):
    def convertToTitle(self, n):      
        m = 0
        val = 26
        
        while n > val:
            m += 1
            
            val += 26 * 26 ** m
          
        s = ""
        
        while m >= 0:
            coeff = n / 26 ** m
            
            if n == 52:
                coeff -= 1
            
            if coeff > 0:  
                if coeff > 26:
                    coeff = 26
                letter = chr(coeff - 1 + ord('A'))
                s += letter
                n -= coeff * 26 ** m  
            
            m -= 1
            
        return s
