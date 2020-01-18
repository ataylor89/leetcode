class Solution(object):
    def toHex(self, num):
        if num == 0:
            return '0'
        
        if num < 0:
            save = num
            num = long(0)
            
            i = 0 
            while i < 32:
                num |= (save & (1 << i))
                i += 1
        
        digits = {i: str(i) for i in range(10)}
        digits[10] = 'a'
        digits[11] = 'b'
        digits[12] = 'c'
        digits[13] = 'd'
        digits[14] = 'e'
        digits[15] = 'f'
        
        e = -1
        while num / 16**(e+1) >= 1:
            e += 1
        
        hexStr = ""
        
        while e >= 0:
            quotient = int(num / 16**e)
            
            hexStr += digits[quotient]
            num -= quotient * 16**e
            e -= 1
        
        return hexStr
