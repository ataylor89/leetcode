from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        if len(s) == 0:
            return -1
        
        counts = defaultdict(lambda: 0)
        
        for c in s:
            counts[c] += 1
        
        i = 0
        while counts[s[i]] > 1:
            i += 1
            
            if i == len(s):
                return -1
            
        return i
