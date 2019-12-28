class Solution(object):
    def strStr(self, haystack, needle):
        ln = len(needle)
        lh = len(haystack)
        
        if ln == 0:
            return 0
        
        for i in range(lh):
            if i + ln > lh:
                break
            
            if haystack[i:i+ln] == needle:
                return i
        
        return -1
