class Solution(object):
    def hammingWeight(self, n):
        binaryString = format(n, 'b')
        hammingWeight = 0
        
        for c in binaryString:
            if c == '1':
                hammingWeight += 1
                
        return hammingWeight
