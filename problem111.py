class Solution(object):

    def minDepth(self, root):
        self.minD = 0
        
        if root != None:
            self.findMinDepth(root, 1)
            
        return self.minD
        
    def findMinDepth(self, node, depth):
        if node.left == None and node.right == None:
            if self.minD == 0:
                self.minD = depth
            else:
                self.minD = min(self.minD, depth)
                
        if node.left != None:
            self.findMinDepth(node.left, depth + 1)
            
        if node.right != None:
            self.findMinDepth(node.right, depth + 1)
