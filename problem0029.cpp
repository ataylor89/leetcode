class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == 0)
            return 0;
        
        if (divisor == 1)
            return dividend;
        
        if (divisor == -1) {
            if (dividend == INT_MIN)
                return INT_MAX;
            
            return 0 - dividend;
        }
        
        int sum = 0;
        int quotient = 0;
        
        if (dividend > 0 && divisor > 0) {
            if (divisor > dividend)
                return 0;
            
            if (divisor == dividend)
                return 1;
            
            if (divisor < (2<<28)) {
                for (int i = 1; (divisor << i) < dividend; i++) {
                    sum = divisor << i;
                    quotient = 2 << (i-1);

                    if ((sum & (2 << 29)) > 0)
                        break;
                }
            }
            
            while (sum < dividend) {
                if (sum > INT_MAX - divisor)
                    return quotient;

                if (sum + divisor <= dividend) 
                    quotient++;

                sum += divisor;
            } 
        }
        
        if (dividend < 0 && divisor < 0) {
            if (divisor < dividend)
                return 0;
            
            if (divisor == dividend)
                return 1;
            
            while (sum > dividend) {
                if (sum < INT_MIN - divisor)
                    return quotient;
                
                if (sum + divisor >= dividend)
                    quotient++;
                
                sum += divisor;
            }
        }
        
        if (dividend < 0 && divisor > 0) {
            while (sum > dividend) {
                if (sum < INT_MIN + divisor)
                    return quotient;
                
                if (sum - divisor >= dividend)
                    quotient--;
                
                sum -= divisor;
            }
        }
        
        if (dividend > 0 && divisor < 0) {
            while (sum < dividend) {
                if (sum > INT_MAX + divisor)
                    return quotient;
                
                if (sum - divisor <= dividend)
                    quotient--;
                
                sum -= divisor;
            }
        }
        
        return quotient; 
    }
};
