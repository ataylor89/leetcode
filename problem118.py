class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return None
    
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1],[1,1]]
        
        pascalsTriangle = [[] for i in range(numRows)]
        pascalsTriangle[0] += [1]
        pascalsTriangle[1] += [1,1]
        
        for j in range(2, numRows):
            for i in range(j+1):
                if i == 0:
                    pascalsTriangle[j].append(1)
                elif i == j:
                    pascalsTriangle[j].append(1)
                else:
                    pascalsTriangle[j].append(pascalsTriangle[j-1][i-1] + pascalsTriangle[j-1][i])
        
        return pascalsTriangle
