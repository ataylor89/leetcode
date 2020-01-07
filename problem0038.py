class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        last = self.countAndSay(n-1)
        ll = len(last)
        
        ans = ""
        i = 0
        
        while i < ll:
            count = 1
            x = last[i]
            
            while (i < ll - 1) and last[i] == last[i+1]:
                count +=1
                i += 1
                    
            i += 1
            
            ans += str(count) + str(x)
            
        return ans
