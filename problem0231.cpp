class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n < 1)
            return false;
        
        for (int i = 0; i <= 31; i++) {
            unsigned int test = 1 << i;
            
            if ((n & test) == n)
                return true;
        }
        return false;
    }
};
