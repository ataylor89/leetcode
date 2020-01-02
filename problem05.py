class Solution(object):
    def longestPalindrome(self, s):
        self.occurrences = {}
        self.longestPalindrome = ""
        
        for i in range(len(s)):
            c = s[i]
            
            if self.occurrences.has_key(c) == False:
                self.occurrences[c] = []
            
            self.occurrences[c].append(i)
            
        for i in range(len(s)):
            c = s[i]
            
            for index in self.occurrences[c]:    
                if i > index:
                    continue
                
                substr = s[i:index+1]
                revSubstr = substr[::-1]
                
                if substr == revSubstr and len(substr) > len(self.longestPalindrome):
                    self.longestPalindrome = substr
                    
        return self.longestPalindrome
