class Solution {
public:
    map<int,bool> results;
    
    bool isHappy(int n) {
        if (n == 1)
            return true;
        
        if (results.find(n) != results.end())
            return false;
        
        results[n] = true;
        string s = to_string(n);
        int m = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int val = s[i] - '0';
            
            if (m > INT_MAX - val * val)
                return false;
                
            m += val * val;
        }
        
        return isHappy(m);
    }
};
