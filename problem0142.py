class Solution(object):
    def detectCycle(self, head):
        refs = {}
        
        while head != None:
            if refs.has_key(id(head)):
                return head
            
            refs[id(head)] = True
            
            head = head.next
        
        return None
