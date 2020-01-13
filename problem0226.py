class Solution(object):
    def invertTree(self, root):
        if root == None or (root.left == None and root.right == None):
            return root
        
        saveLeft = root.left
        root.left = root.right
        root.right = saveLeft
        
        self.invertTree(root.left)    
        self.invertTree(root.right)
        
        return root
