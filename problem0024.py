class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        
        a,b = head, head.next
        
        a.next = b.next
        b.next = a
        
        if a.next != None and a.next.next != None:
            self._swapPairs(a, a.next, a.next.next)
        
        return b
    
    def _swapPairs(self, a, b, c):
        a.next = c
        b.next = c.next
        c.next = b
        
        if b.next != None and b.next.next != None:
            self._swapPairs(b, b.next, b.next.next)
