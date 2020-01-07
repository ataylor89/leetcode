class Solution(object):
    def plusOne(self, digits):
        lastDigit = digits[-1]
        
        if lastDigit < 9:
            digits[-1] = lastDigit + 1
            return digits
        
        if lastDigit == 9 and len(digits) == 1:
            return [1, 0]
        
        i = len(digits) - 1

        while i >= 0:
            if digits[i] == 9 and i > 0:
                digits[i] = 0
                i -= 1
            elif digits[i] == 9 and i == 0:
                digits[i] = 0
                digits.insert(0, 1)
                break
            else:
                digits[i] += 1
                break
            
        return digits
