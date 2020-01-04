class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex < 0:
            return None
        
        # Pascal's triangle
        triangle = [[] for x in range(rowIndex+1)]
        triangle[0] += [1]
        
        if rowIndex == 0:
            return triangle[0]
        
        triangle[1] += [1,1]
        
        if rowIndex == 1:
            return triangle[1]
        
        i = 2
        
        while i <= rowIndex:
            for j in range(i+1):
                if j == 0 or j == i:
                    triangle[i].append(1)
                else:
                    triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
                    
            i += 1
                    
        return triangle[rowIndex]
