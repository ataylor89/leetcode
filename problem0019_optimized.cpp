/*
 * I looked at a solution to this problem and found an optimized approach using O(1) memory
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* node = head;
        ListNode* tail = head;
        
        int iters = 0;
        while (tail->next != NULL) {
            if (iters >= n)
                node = node->next;
            tail = tail->next;
            iters++;
        }
        
        if (node == head && iters < n)
            return head->next;
        
        node->next = node->next->next;
        return head;
    }
};
