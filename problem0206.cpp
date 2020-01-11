class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL)
            return NULL;
        
        if (head->next == NULL)
            return head;
        
        vector<ListNode*> refs;
 
        while (head != NULL) {
            refs.push_back(head);
            head = head->next;
        }
        
        for (int i = refs.size()-1; i >= 0; i--) {
            if (i == 0)
                refs[i]->next = NULL;
            else
                refs[i]->next = refs[i-1];
        }
        
        return refs[refs.size()-1];
    }
};
