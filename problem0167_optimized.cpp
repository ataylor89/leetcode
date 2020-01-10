class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> answers;
        
        if (numbers.size() < 2)
            return answers;
        
        map<int, int> map;
        
        for (int i = 0; i < numbers.size(); i++) 
            map[numbers[i]] = i;
        
        for (int i = 0; i < numbers.size(); i++) {
            if (map.find(target - numbers[i]) != map.end()) {
                int j = map[target-numbers[i]];
                answers.push_back(i+1);
                answers.push_back(j+1);
                return answers;
            }
        }
        
        return answers;
    }
};
