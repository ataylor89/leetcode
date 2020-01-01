class Solution(object):
    
    def maxDepth(self, root):
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        depthL = 0
        depthR = 0
        
        if root.left != None:
            depthL = 1 + self.maxDepth(root.left)
            
        if root.right != None:
            depthR = 1 + self.maxDepth(root.right)
            
        localMax = max(depthL, depthR)
        
        return localMax
