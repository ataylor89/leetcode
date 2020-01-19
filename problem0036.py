class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            if self.isValidRow(board, i) == False:
                return False
            if self.isValidColumn(board, i) == False:
                return False
        
        for j in range(3):
            for i in range(3):
                if self.isValidBox(board, i*3, j*3) == False:
                    return False
        
        return True
        
    def isValidRow(self, board, rowNum):
        row = board[rowNum]
        counts = {i:1 for i in range(1, 10)}
        
        for c in row:
            if c.isdigit():
                if counts[int(c)] < 1:
                    return False
                counts[int(c)] = 0
                
        return True
    
    def isValidColumn(self, board, colNum):
        counts = {i:1 for i in range(1, 10)}
        
        for i in range(9):
            c = board[i][colNum]
            
            if c.isdigit():
                if counts[int(c)] < 1:
                    return False
                counts[int(c)] = 0
                
        return True
        
    def isValidBox(self, board, x, y):
        counts = {i:1 for i in range(1, 10)}
        
        for j in range(y, y+3):
            for i in range(x, x+3):
                c = board[j][i]
                if c.isdigit():
                    if counts[int(c)] < 1:
                        return False
                    counts[int(c)] = 0
                    
        return True
