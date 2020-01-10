class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL || headB == NULL)
            return NULL;
        
        map<ListNode*,bool> m;
        
        while (headA != NULL) {
            m[headA] = true;
            headA = headA->next;
        }
        
        while (headB != NULL) {
            if (m.find(headB) != m.end()) 
                return headB;
            
            headB = headB->next;
        }
        
        return NULL;
    }
};
