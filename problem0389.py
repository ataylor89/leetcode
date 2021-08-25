from collections import defaultdict
class Solution(object):
    def findTheDifference(self, s, t):
        smap = defaultdict(lambda: 0)
        tmap = defaultdict(lambda: 0)
        
        for letter in s:
            smap[letter] += 1
            
        for letter in t:
            tmap[letter] += 1
            
            if tmap[letter] > smap[letter]:
                return letter
            
        return None
