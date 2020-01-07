class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        sum = 0
        
        n = 0
        
        while l1 != None:
            sum += l1.val * 10 ** n
            n += 1
            l1 = l1.next
        
        n = 0
        
        while l2 != None:
            sum += l2.val * 10 ** n
            n += 1
            l2 = l2.next
                      
        s = str(sum)[::-1]
        length = len(s)
        
        head = ListNode(None)
        tail = head
        
        for i in range(length):
            tail.val = int(s[i])
            
            if i < length - 1:
                tail.next = ListNode(None)
                tail = tail.next
                
        return head
