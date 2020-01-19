class Solution(object):
    def getSum(self, a, b):
        stack = []
        
        if a == -1 * b:
            return 0
        
        if a > 0 and b > 0:
            for i in range(0, a):
                stack.append(1)
            for i in range(0, b):
                stack.append(1)
        
        if a > 0 and b < 0:
            if a > -1 * b:
                for i in range(-1*b, a):
                    stack.append(1)
            
            else:
                for i in range(a, -1*b):
                    stack.append(-1)
        
        if a < 0 and b > 0:
            if b > -1 * a:
                for i in range(-1*a, b):
                    stack.append(1)
            else:
                for i in range(b, -1*a):
                    stack.append(-1)
        
        if a < 0 and b < 0:
            for i in range(0, a, -1):
                stack.append(-1)
            for i in range(0, b, -1):
                stack.append(-1)
                
        if a == 0:
            if b < 0:
                for i in range(0, b, -1):
                    stack.append(-1)
            else:
                for i in range(0, b):
                    stack.append(1)
        
        if b == 0:
            if a < 0:
                for i in range(0, a, -1):
                    stack.append(-1)
            else:
                for i in range(0, a):
                    stack.append(1)
        
        if len(stack) == 0:
            return 0
        
        return len(stack) * stack[0]
