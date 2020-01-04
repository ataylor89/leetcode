class Solution(object):
    def intToRoman(self, num):
        romanNumerals = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        
        snum = str(num)
        lsnum = len(snum)
        
        romanStr = ""
        
        for i in range(lsnum):
            digit = int(snum[i])
            
            if digit == 0:
                continue
            
            elif digit < 4:
                romanNumeral = romanNumerals[10 ** (lsnum-1-i)]
                romanStr += romanNumeral * digit
                
            elif digit == 4:
                romanNumeral1 = romanNumerals[10 ** (lsnum-1-i)]
                romanNumeral2 = romanNumerals[5 * 10 ** (lsnum-1-i)]
                romanStr += romanNumeral1 + romanNumeral2
                
            elif digit == 5:
                romanNumeral = romanNumerals[5 * 10 ** (lsnum-1-i)]
                romanStr += romanNumeral
                
            elif digit < 9:
                romanNumeral1 = romanNumerals[5 * 10 ** (lsnum-1-i)]
                romanNumeral2 = romanNumerals[10 ** (lsnum-1-i)]
                romanStr += romanNumeral1 + romanNumeral2 * (digit - 5)
                
            elif digit == 9:
                romanNumeral1 = romanNumerals[10 ** (lsnum-1-i)]
                romanNumeral2 = romanNumerals[10 ** (lsnum-i)]
                romanStr += romanNumeral1 + romanNumeral2
                
        return romanStr
