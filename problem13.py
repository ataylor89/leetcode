class Solution(object):
    def romanToInt(self, s):
        roman_numerals = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        length = len(s)
        integer = 0
        
        for i in range(length):
            if i == length - 1:
                integer += roman_numerals[s[i]]   
                
            elif s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                integer -= roman_numerals[s[i]]
            
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                integer -= roman_numerals[s[i]]
                
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                integer -= roman_numerals[s[i]]
            
            else:
                integer += roman_numerals[s[i]]
                
        return integer
