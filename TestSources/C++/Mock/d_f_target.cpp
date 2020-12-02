class Solution {
private:
    
    #define min(a, b) ((a) < (b) ? (a) : (b))
    long long mx = 1e9 + 7;
    
    long long factorial(int n) {
        if (n == 1)
            return 1;
        return n * factorial(n - 1) % mx;
    }
    
public:
    int numRollsToTarget(int d, int f, int target) {
        long long ans = 0;
        
        if(target > f * d)
            return 0;
        else if(target == f * d)
            return 1;
        
        if(d == 1)
            return 1;
        
        int min = 1;
        int max = min(f, (target - d));
        int no_vals = max - min;
        ans = ((factorial(no_vals) % mx) / ((factorial(no_vals - d) * factorial(d)) % mx)) % mx;
        
        return (ans % mx);
    }
};