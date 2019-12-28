class Solution(object):
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        
        values = {}
        values[head.val] = True
        
        tail = head
        
        while tail != None:
            node = tail.next
            
            if node == None:
                break
            
            if values.has_key(node.val):
                tail.next = node.next
                continue
                
            values[node.val] = True
            tail = node
            
        return head
