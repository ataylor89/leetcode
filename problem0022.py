class Solution(object):
    def generateParenthesis(self, n):
        self.solutions = []
        
        self.generateString("", n, n)
        
        return self.solutions
    
    def generateString(self, str, nl, nr):
        if nl == 0 and nr == 0:
            self.solutions.append(str)
            return
        
        elif nl == 0 and nr > 0:
            str += ')' * nr
            self.solutions.append(str)
            return
        
        if nl > 0:
            self.generateString(str + '(', nl-1, nr)
            
        if nl < nr:
            self.generateString(str + ')', nl, nr-1)
