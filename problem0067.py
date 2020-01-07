class Solution(object):
    def addBinary(self, a, b):        
        valA = int(a, 2)
        valB = int(b, 2)
        
        sum = valA + valB
        return "{0:b}".format(sum)
