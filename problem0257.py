class Solution(object):
    def binaryTreePaths(self, root):
        if root == None:
            return None
        
        path = str(root.val)
        
        if root.left == None and root.right == None:
            return [path]
        
        self.paths = []
        
        if root.left != None:
            self.traverse(root.left, path)
        
        if root.right != None:
            self.traverse(root.right, path)
            
        return self.paths
        
    def traverse(self, node, path):
        path += "->" + str(node.val)
        
        if node.left == None and node.right == None:
            self.paths.append(path)
            return
            
        if node.left != None:
            self.traverse(node.left, path)
        
        if node.right != None:
            self.traverse(node.right, path)
