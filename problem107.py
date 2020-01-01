class Solution(object):
    
    def levelOrderBottom(self, root):
        self.topDownTraversal = []
        
        if root == None:
            return []
        
        self.traverse(root, 0)
        
        return self.topDownTraversal[::-1]
    
    def traverse(self, root, level):
        if len(self.topDownTraversal) <= level:
            self.topDownTraversal.append([])
            
        self.topDownTraversal[level].append(root.val if root != None else None)
        
        if root.left != None:
            self.traverse(root.left, level + 1)
        
        if root.right != None:
            self.traverse(root.right, level + 1)
