class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        pathP = self.pathTo(root, p)
        pathQ = self.pathTo(root, q)
        
        return self._lowestCommonAncestor(root, p, q, pathP, pathQ)
    
    def _lowestCommonAncestor(self, node, p, q, pathP, pathQ):
        if len(pathP) == 0 or len(pathQ) == 0:
            return node
        
        a,b = pathP.pop(0), pathQ.pop(0)
        
        if a != b:
            return node
        
        if a == 0:
            return self._lowestCommonAncestor(node.left, p, q, pathP, pathQ)
        
        else:
            return self._lowestCommonAncestor(node.right, p, q, pathP, pathQ)
        
        
    def pathTo(self, root, target):
        if root.val == target.val:
            return []
        
        if root.val < target.val:
            return [1] + self.pathTo(root.right, target)

        if root.val > target.val:
            return [0] + self.pathTo(root.left, target)
