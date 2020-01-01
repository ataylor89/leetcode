class Solution(object):
    
    def sortedArrayToBST(self, nums):
        self.rootNode = TreeNode(None)
        
        if len(nums) == 0:
            return None
        
        self.insertIntoTree(nums, self.rootNode)
        
        return self.rootNode
    
    def insertIntoTree(self, nums, node):
        ln = len(nums)
        
        if ln == 0:
            return
        
        medianIndex = int(ln / 2)
        node.val = nums[medianIndex]
        
        if medianIndex > 0:
            node.left = TreeNode(None)
            self.insertIntoTree(nums[0:medianIndex], node.left)
        
        if medianIndex < ln - 1:
            node.right = TreeNode(None)
            self.insertIntoTree(nums[medianIndex+1:ln], node.right)
