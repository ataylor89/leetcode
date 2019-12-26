class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        
        longest_prefix = ""
        
        first_str = strs[0]
        
        for i in range(len(first_str)):
            for str in strs:
                if len(str) <= i:
                    return longest_prefix
                if str[i] != first_str[i]:
                    return longest_prefix
                
            longest_prefix += first_str[i]
            
        return longest_prefix
