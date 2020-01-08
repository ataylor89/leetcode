class Solution(object):
    def hasCycle(self, head):
        if (head == None):
            return False
        
        self.vals = {}
        self.hasOne = False
        
        self.traverse(head)
        
        return self.hasOne
        
    def traverse(self, head):
        if self.hasOne == True:
            return
        
        if self.vals.has_key(id(head)):
            self.hasOne = True
            return
        
        self.vals[id(head)] = True
        
        if head.next != None:
            self.traverse(head.next)
