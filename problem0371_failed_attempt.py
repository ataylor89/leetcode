# This attempt fails because it is too slow
class Solution(object):
    def getSum(self, a, b):
        stack = []
        if a >= 0:
            for i in range(0, a):
                stack.append(1)
                
            if b > 0:
                for i in range(0, b):
                    stack.append(1)
                    
            if b < 0:
                if -1 * b  >= a:
                    for i in range(0, a):
                        stack.pop(0)
                    
                    for i in range(a, -1 * b):
                        stack.append(-1)
                else:
                    for i in range(0, b, -1):
                        stack.pop(0)
        
        elif a < 0:
            for i in range(0, a, -1):
                stack.append(-1)
                
            if b > 0:
                if -1 * a >= b:
                    for i in range(0, b):
                        stack.pop(0)
                
                else:
                    for i in range(0, a, -1):
                        stack.pop(0)
                    
                    for i in range(-1*a, b):
                        stack.append(1)
            
            if b < 0:
                for i in range(0, b, -1):
                    stack.append(-1)
                    
        if len(stack) == 0:
            return 0
        
        return len(stack) * stack[0]
