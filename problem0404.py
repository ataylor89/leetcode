class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root == None:
            return 0
        
        return self._sumOfLeftLeaves(root, False)
    
    def _sumOfLeftLeaves(self, node, isLeft):
        if node.left == None and node.right == None:
            return node.val if isLeft == True else 0
        
        s = 0
        
        if node.left != None:
            s += self._sumOfLeftLeaves(node.left, True)
        
        if node.right != None:
            s += self._sumOfLeftLeaves(node.right, False)
            
        return s
