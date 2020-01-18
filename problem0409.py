from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        counts = defaultdict(lambda: 0)
        
        for letter in s:
            counts[letter] += 1
           
        lengthOfLongest = 0
        hasMedian = False   
        
        for letter in counts:
            if counts[letter] % 2 == 0:
                lengthOfLongest += counts[letter]
            
            elif counts[letter] > 1:
                lengthOfLongest += (counts[letter] - 1)
            
            if counts[letter] % 2 == 1 and hasMedian == False:
                lengthOfLongest += 1
                hasMedian = True
                
        return lengthOfLongest
