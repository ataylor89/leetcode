class Solution(object):
    def titleToNumber(self, s):
        
        columnNumber = 0
        
        for i in range(len(s)):
            n = len(s) - i - 1
            
            letterVal = ord(s[i]) - ord('A') + 1
            
            columnNumber += letterVal * 26 ** n
            
        return columnNumber;
