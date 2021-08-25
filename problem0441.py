class Solution:
    def arrangeCoins(self, n: int) -> int:
        staircase = []
        
        m = n
        
        for i in range(1, n+1):
            if i <= m:
                staircase.append(i)
                m -= i
            else:
                return len(staircase)
            
        return len(staircase)
