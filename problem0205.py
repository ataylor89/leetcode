class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        # m = mappings, r = reverse mappings
        m,r = {}, {}
        
        i = 0
        while i < len(s):
            a,b = s[i], t[i]
            
            if a != b:
                # b cannot be mapped to from two different characters
                if r.has_key(b) and r[b] != a:
                    return False
            
            m[a] = b
            r[b] = a
            i += 1
        
        i = 0
        s2 = ""
        while i < len(s):
            s2 += m[s[i]]
            i += 1
            
        return s2 == t
