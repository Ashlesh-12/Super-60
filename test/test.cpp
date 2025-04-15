// 1. Generate an array of 100 integers based on the below series:
// 1 2 5 10 17 26 37 50 65 82
// 101… (100 

#include<iostream>
using namespace std;
int main()
{
    int a[200],i;
    for(i=0;i<100;i++)
    {
        a[i-1]=i*i-i+1;
    }
    for(i=0;i<100;i++)
    {
        cout<<a[i]<<" ";
    }
    return 0;
}