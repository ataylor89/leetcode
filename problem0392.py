class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False
        
        i = 0
        while len(s) > 0 and i < len(t):
            if s[0] == t[i]:
                s = s[1:]
            i += 1
        
        return len(s) == 0
