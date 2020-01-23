class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        s = 0
        
        digits = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        
        for i in range(0, max(len(num1), len(num2))):
            if i < len(num1):
                s += digits[num1[i]] * 10 ** i
            if i < len(num2):
                s += digits[num2[i]] * 10 ** i
                
        return str(s)
