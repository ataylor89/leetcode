class Solution:
    def countSegments(self, s: str) -> int:
        inSegment = False
        count = 0
        
        for c in s:
            if c.isspace():
                inSegment = False
            
            elif inSegment == False:
                inSegment = True
                count += 1
        
        return count
