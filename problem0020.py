class Solution(object):
    def isValid(self, s):
        if len(s) == 0:
            return True
        
        if (len(s) % 2 != 0):
            return False
        
        stack = []
        
        mirror = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                
                open_bracket = stack.pop()
                
                if mirror[open_bracket] != c:
                    return False
                
        return len(stack) == 0
