class Solution {
public:
    int tribonacci(int n) {
        int a = 0, b = 1, c = 1, tNum;
        
        if(n<1)
            return 0;
        if(n<2)
            return 1;
        
        for(int i=2; i<n; i++)
        {
            tNum = a+b+c;
            a = b;
            b = c;
            c = tNum;
        }

        return tNum;
    }
};