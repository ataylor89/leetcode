class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longestSubstring = ""
        substring = ""
        substring_index = 0
        usedLetters = {}
        lengthS = len(s)
        
        for i in range(lengthS):                
            letter = s[i]  
            haskey = usedLetters.has_key(letter)
        
            if haskey and usedLetters[letter] >= substring_index:   
                if len(substring) > len(longestSubstring):
                    longestSubstring = substring
                
                lastIndex = usedLetters[letter]
                substring = s[lastIndex+1:i+1]
                substring_index = lastIndex + 1
                
            else:
                substring += letter
                
                if len(substring) > len(longestSubstring):
                    longestSubstring = substring
         
            usedLetters[letter] = i

        return len(longestSubstring)
