class Solution {
public:
    int fib(int n) {
        if(n==0) 
            return 0;
        int fNum = 1, a=1, b=0;
        
        for(int i=1; i<n; i++)
        {
            fNum = a+b; 
            b = a;
            a = fNum;
        }
        
        return fNum;
    }
};

/*
    1, 1, 2, 3, 5, 8, 13, 21
    1, 2, 4, 7, 12, 20, 33, 54
    
*/