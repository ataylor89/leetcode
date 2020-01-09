# I optimized this after seeing someone else's solution
# This runs in constant time
class MinStack(object):
 
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        
        if len(self.minStack) == 0:
            self.minStack.append(x)
        elif x <= self.minStack[-1]:
            self.minStack.append(x)
            
    def pop(self):
        if len(self.stack) == 0:
            return None
        
        p = self.stack.pop(-1)
        if p == self.minStack[-1]:
            self.minStack.pop(-1)
            
        return p

    def top(self):
        if len(self.stack) == 0:
            return None
        
        return self.stack[-1]
        
    def getMin(self):
        if len(self.stack) == 0:
            return None
        
        return self.minStack[-1]
