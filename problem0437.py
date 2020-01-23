class Solution:
    
    def __init__(self):
        self.numPaths = 0
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root != None:
            self._pathSum(root, sum, [])
        
        return self.numPaths
        
    def _pathSum(self, node, target, runningSums):
        for i in range(len(runningSums)):
            runningSums[i] += node.val
            
            if runningSums[i] == target:
                self.numPaths += 1
        
        runningSums.append(node.val)
        
        if node.val == target:
            self.numPaths += 1
        
        if node.left != None:
            self._pathSum(node.left, target, list(runningSums))
            
        if node.right != None:
            self._pathSum(node.right, target, list(runningSums))
