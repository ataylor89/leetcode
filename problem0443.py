class Solution:
    def compress(self, chars: List[str]) -> int:      
        count = 0
        
        j = 0
        while j < len(chars):
            c = chars[j]
            k = j+1
            
            subCount = 1
            
            while k < len(chars) and chars[k] == c:
                subCount += 1
                chars.pop(k)
                
            j += 1
            if subCount > 1:
                for x in str(subCount):
                    chars.insert(j, x)
                    j += 1
        
        return j
