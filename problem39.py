import sets

class Solution(object):
    def combinationSum(self, candidates, target):
        self.solutions = sets.Set()
        
        for c in candidates:
            self.findCombination(candidates, [c], target)
            
        return self.solutions
        
    def findCombination(self, candidates, combination, target):
        S = sum(combination)
        
        if S == target:
            combination.sort()
            self.solutions.add(tuple(combination))
            return
        
        elif S < target:
            for c in candidates:
                if c + S <= target:
                    self.findCombination(candidates, combination + [c], target)
