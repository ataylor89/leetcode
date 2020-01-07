class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxValue = 0;
        
        if (prices.size() < 2)
            return 0;
        
        for (int i = 0; i < prices.size() - 1; i++) {
            for (int j = i; j < prices.size(); j++) {
                int profit = prices[j] - prices[i];
                
                if (profit > maxValue)
                    maxValue = profit;
            }
        }
        
        return maxValue;
    }
};
