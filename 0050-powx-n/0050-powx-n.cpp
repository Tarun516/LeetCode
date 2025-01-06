class Solution {

private:
    double power(double x, long n)
    {
        if ( n == 0) return 1.0;
        else if(n == 1) return x;

        if(n%2 == 0) //even number
            return power(x*x, n/2);

        //odd number
        return x * power(x,n-1);
    }

public:
    double myPow(double x, int n) {

        long num = n;
        if(num < 0)
            return (1.0 / power(x, -1 * num));
        
        return power(x,num);        

    }
};