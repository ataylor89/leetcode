class Solution(object):
    def isSymmetric(self, root):
        nodesByLevel = {}
        
        self.treeAsList(root, 0, nodesByLevel)
        
        i = 0
        while nodesByLevel.has_key(i):
            nodes = nodesByLevel[i]
            revNodes = nodes[::-1]
            
            for j in range(len(nodes)):
                node = nodes[j]
                revNode = revNodes[j]
                
                if node != revNode:
                    return False
                
            i += 1
        
        return True
                
    def treeAsList(self, root, level, nodesByLevel):
        if nodesByLevel.has_key(level) == False:
            nodesByLevel[level] = []
        
        nodesByLevel[level].append(root.val if root != None else None)
        
        if root != None:
            self.treeAsList(root.left, level + 1, nodesByLevel)
            self.treeAsList(root.right, level + 1, nodesByLevel)
