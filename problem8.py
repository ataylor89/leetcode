class Solution(object):
    def myAtoi(self, str):
        digitValues = {
            '0' : 0,
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9
        }
        
        INT_MAX = 2**31 - 1
        INT_MIN = (-2)**31
        
        str = str.strip()
        
        if len(str) == 0:
            return 0
        
        negative = False
        
        if str[0] == '-':
            negative = True
            str = str[1:]
            
        elif str[0] == '+':
            negative = False
            str = str[1:]
        
        for i in range(len(str)):
            if str[i].isdigit() == False:
                str = str[0:i]
                break
        
        numDigits = len(str)
        
        val = 0
        
        for i in range(numDigits):
            dv = digitValues[str[i]] * 10 ** (numDigits - 1 - i)
            
            val += dv if negative == False else -1 * dv
            
            if val >= INT_MAX:
                return INT_MAX
            
            if val <= INT_MIN:
                return INT_MIN
            
        return val
