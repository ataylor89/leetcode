from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        counts = defaultdict(lambda: 0)
        
        for letter in magazine:
            counts[letter] += 1
            
        for letter in ransomNote:
            if counts[letter] > 0:
                counts[letter] -= 1
            else:
                return False
        
        return True
