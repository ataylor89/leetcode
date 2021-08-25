class Solution(object):
    def myPow(self, x, n):
        INT_MIN = -2147483648;
        INT_MAX = 2147483647;
        FLOAT_MIN = 0.000000000000000000000000000001;
        
        if x == 1:
            return 1
        
        if x == -1:
            return 1 if n % 2 == 0 else -1
                        
        if n == 0:
            return 1
        
        if n > 0:
            product = 1
        
            while n > 0:
                product *= x
                n -= 1
                
                if product > 0 and product < FLOAT_MIN:
                    return 0
                
                if product < 0 and product > -1 and product > -1 * FLOAT_MIN:
                    return 0
                
                if product <= INT_MIN:
                    return 0
                
                if product >= INT_MAX:
                    return 0
            
            return product
        
        if n < 0:
            product = 1
            
            while n < 0:
                product /= x
                n += 1
                
                if product > 0 and product < FLOAT_MIN:
                    return 0
                
                if product < 0 and product > -1 and product > -1 * FLOAT_MIN:
                    return 0
                
                if product <= INT_MIN:
                    return 0
                
                if product >= INT_MAX:
                    return 0
            
            return product
