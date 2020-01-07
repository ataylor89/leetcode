class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        
        head = ListNode(None)
        tail = head
        
        while l1 != None or l2 != None:           
            if l1 != None and l2 != None:
                if l1.val <= l2.val:
                    tail.val = l1.val
                    l1 = l1.next
                else:
                    tail.val = l2.val
                    l2 = l2.next
                               
            elif l1 != None:
                tail.val = l1.val
                l1 = l1.next
                
            elif l2 != None:
                tail.val = l2.val
                l2 = l2.next
                
            if l1 != None or l2 != None:
                tail.next = ListNode(None)
                tail = tail.next
        
        return head
