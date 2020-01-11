class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int,int> m;
        
        for (int i = 0; i < nums.size(); i++) {
            if (m.find(nums[i]) != m.end()) {
                int j = m[nums[i]];
                
                if (i - j <= k)
                    return true; 
            }
            m[nums[i]] = i;
        }
        
        return false;
    }
};
