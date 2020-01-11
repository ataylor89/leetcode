class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        unsigned int result = 0xffffffff;
        
        for (int i = m; i <= n; i++) {
            result = result & i;
            
            if (result == 0 || i == 2147483647)
                break;
        }
        
        return result;
    }
};
