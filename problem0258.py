class Solution(object):
    def addDigits(self, num):
        s = str(num)
        
        if len(s) == 1:
            return num
        
        result = 0
        
        for c in s:
            result += int(c)
            
        return self.addDigits(result)
