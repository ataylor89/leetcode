class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> answers;
        
        if (numbers.size() < 2)
            return answers;
        
        for (int i = 0; i < numbers.size() - 1; i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                if (numbers[i] + numbers[j] == target) {
                    answers.push_back(i+1);
                    answers.push_back(j+1);
                    return answers;
                }
                if (numbers[i] + numbers[j] > target) 
                    break;
            }
        }
        
        return answers;
    }
};
