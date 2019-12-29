class Solution(object):
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        
        elif p == None or q == None:
            return False
        
        if (p.left == None and p.right == None and q.left == None and q.right == None):
            return p.val == q.val
        
        elif (p.left == None and p.right == None) or (q.left == None and q.right == None):
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
