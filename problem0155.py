class MinStack(object):
 
    def __init__(self):
        self.stack = []
        self.sorted = []

    def push(self, x):
        self.stack.append(x)
        self.sorted = sorted(self.stack)
            
    def pop(self):
        if len(self.stack) == 0:
            return None
        
        p = self.stack.pop(-1)
        self.sorted = sorted(self.stack)
        return p

    def top(self):
        if len(self.stack) == 0:
            return None
        
        return self.stack[-1]
        
    def getMin(self):
        if len(self.stack) == 0:
            return None
        
        return self.sorted[0]
