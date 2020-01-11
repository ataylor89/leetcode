class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        vector<ListNode*> nodes;
        
        ListNode* tail = head;
        
        while (tail != NULL) {
            nodes.push_back(tail);
            tail = tail->next;
        }
                
        if (n == nodes.size()) 
            return head->next;
        
        ListNode* node = nodes[nodes.size() - n - 1];
        node->next = node->next->next;
        
        return head;
    }
};
