class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        while (head != NULL && head->val == val)
            head = head->next;
        
        if (head == NULL)
            return head;
        
        ListNode* tail = head;
        
        while (tail != NULL && tail->next != NULL) {
            if (tail->next->val == val)
                tail->next = tail->next->next;
            else
                tail = tail->next;
        }
        
        return head;
    }
};
