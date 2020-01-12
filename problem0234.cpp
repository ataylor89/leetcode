class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return true;
        
        vector<ListNode*> refs;
        
        while (head != NULL) {
            refs.push_back(head);
            head = head->next;
        }
        
        for (int i = 0; i < refs.size() / 2; i++) 
            if (refs[i]->val != refs[refs.size()-1-i]->val)
                return false;
        
        return true;
    }
};
