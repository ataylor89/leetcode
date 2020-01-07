class Solution(object):

    def isBalanced(self, root):
        if root == None:
            return True
        
        self.assignHeight(root)
        
        if root.left == None and root.right == None:
            return True
        
        elif root.left != None and root.right == None:
            return root.left.height == 0
        
        elif root.right != None and root.left == None:
            return root.right.height == 0
        
        else:
            lh = root.left.height
            rh = root.right.height
            
            bl = self.isBalanced(root.left)
            br = self.isBalanced(root.right)
            
            return abs(lh - rh) <= 1 and bl and br
        
    def assignHeight(self, node):
        if node == None:
            return
        
        node.height = None
        
        if node.left == None and node.right == None:
            node.height = 0
        
        if node.left != None and node.right == None:
            self.assignHeight(node.left)
            
            node.height = 1 + node.left.height
        
        elif node.right != None and node.left == None:
            self.assignHeight(node.right)
            
            node.height = 1 + node.right.height
        
        elif node.left != None and node.right != None:
            self.assignHeight(node.left)
            self.assignHeight(node.right)
            
            node.height = 1 + max(node.left.height, node.right.height)
