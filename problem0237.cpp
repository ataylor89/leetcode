class Solution {
public:
    void deleteNode(ListNode* node) {
        if (node->next == NULL)
            return;
        
        node->val = node->next->val;
        
        node->next = node->next->next;
    }
};