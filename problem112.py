class Solution(object):
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        
        self.targetSum = sum
        self.hasPath = False
        
        self.traverseAndSum(root, 0)
        
        return self.hasPath
        
    def traverseAndSum(self, node, pathSum):
        if self.hasPath == True:
            return
        
        pathSum += node.val
        
        if node.left == None and node.right == None and pathSum == self.targetSum:
            self.hasPath = True
            
        if node.left != None:
            self.traverseAndSum(node.left, pathSum)
            
        if node.right != None:
            self.traverseAndSum(node.right, pathSum)
