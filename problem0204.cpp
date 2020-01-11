class Solution {
public:
    int countPrimes(int n) {
        if (n < 2)
            return 0;
                
        vector<bool> sieve(n+1, false); // sieve[x] is false if x is prime, true otherwise
        sieve[0] = true;
        sieve[1] = true;
        
        for (int i = 2; i <= n/2; i++) 
            for (int j = 2; i * j <= n; j++) 
                sieve[i*j] = true;

        int numPrimes = 0;
        
        for (int i = 2; i < n; i++)
            if (!sieve[i])
                numPrimes++;
        
        return numPrimes;
    }
};
