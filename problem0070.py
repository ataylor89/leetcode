class Solution(object):
    
    solutions = {}
    
    def climbStairs(self, n):
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        if n > 2:
            if self.solutions.has_key(n):
                return self.solutions[n]
            
            self.solutions[n-1] = self.climbStairs(n-1)
            self.solutions[n-2] = self.climbStairs(n-2)
            
            return self.solutions[n-1] + self.solutions[n-2]
