/*
 * This is a dynamic programming problem that uses stored results of subproblems
 * to optimize the recursive calls to the iterate function.
 */
class Solution {
public:
    
    int maxAmount = 0;
    map<int, int> m;
    
    int rob(vector<int>& nums) {
        if (nums.size() == 0)
            return NULL;
        
        if (nums.size() == 1)
            return nums[0];
        
        for (int i = nums.size() - 1; i >= 0; i--) 
            iterate(nums, i, i, 0);
        
        return maxAmount;
    }
    
    void iterate(vector<int>& nums, int start, int i, int runningSum) {
        if (i != start && m.find(i) != m.end()) {
            runningSum += m[i];
            
            if (runningSum > maxAmount)
                maxAmount = runningSum;
            
            if (m.find(start) == m.end() || runningSum > m[start]) 
                m[start] = runningSum;
            
            return;
        }
            
        runningSum += nums[i];
        
        if (runningSum > maxAmount)
            maxAmount = runningSum;
                  
        i += 2;
        
        if (i >= nums.size()) 
            if (m.find(start) == m.end() || runningSum > m[start]) 
                m[start] = runningSum;
            
        while (i < nums.size()) {
            iterate(nums, start, i, runningSum);
            i += 1;
        }
    }
};
