class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map<int,int> m;
        map<int,int>::iterator itm;
        
        for (vector<int>::iterator itv = nums.begin(); itv != nums.end(); ++itv) {
            int val = *itv;
            
            itm = m.find(val);
            
            if (itm == m.end()) {
                m[val] = 1;
            }
            else {
                m.erase(itm);
            }
        }
        
        itm = m.begin();
        
        return itm->first;
    }
};
