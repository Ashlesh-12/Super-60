// #include<iostream>
// using namespace std;
// int main()
// {
//     int rem,n,r=0,ans;
//     cout<<"n=";
//     cin>>n;
//     while(n!=0)
//     {
//         if(n>1000000&&n<10000000)
//         {
//             ans=n/1000000;
//         }
//         if(n>100000&&n<1000000)
//         {
//             ans=n/100000;
//         }
//         if(n>10000&&n<100000)
//         {
//             ans=n/10000;
//         }
//         if(n>1000&&n<10000)
//         {
//             ans=n/1000;
//         }
//        else if(n>100&&n<1000)
//         {
//         ans=n/100;
//         }
//         else if(n<100&&n>10)
//         {
//             ans=n/10;
//         }
//          else if(n<10)
//         {
//             ans=n;
//         }
//         if(ans==1)
//         {
//             cout<<"one ";
//         }
//         else if(ans==2)
//         {
//             cout<<"Two ";
//         }
//         else if(ans==3)
//         {
//             cout<<"Three ";
//         }
//         else if(ans==4)
//         {
//             cout<<"Four ";
//         }
//         else if(ans==5)
//         {
//             cout<<"Five ";
//         }
//         else if(ans==6)
//         {
//             cout<<"Six ";
//         }
//         else if(ans==7)
//         {
//             cout<<"Seven ";
//         }
//             else if(ans==8)
//         {
//             cout<<"Eight ";
//         }
//         else if(ans==9)
//         {
//             cout<<"Nine ";
//         }
//           if(n<1000000&&n>100000)
//         {
//          n=n%100000;
//         }
//          else if(n<100000&&n>10000)
//         {
//          n=n%10000;
//         }
//          else if(n<10000&&n>1000)
//         {
//          n=n%1000;
//         }
//         else if(n<1000&&n>100)
//         {
//          n=n%100;
//         }
//         else if(n<100&&n>10)
//         {
//             n=n%10;
//         }
//         else if(n<10)
//         {
//             exit(0);
//         }
//         }
      
//     }

// #include<iostream>
// using namespace std;
// int main()
// {
//     int n,i,j=2;
//     cout<<"n= ";
//     cin>>n;
//     for(i=1;i<n;)
//     {
//         cout<<i<<" ";
//         j=2*j;
//         i=i+j;

//     }
// }

// #include<iostream>
// using namespace std;
// int main()
// {
//     int n,bin=0,i,rem,bina=1;
//     cout<<"n= ";
//     cin>>n;
//     while(n!=0)
//     {
//         rem=n%2;
//         n=n/2;
//         bin=bin+(rem*bina);
//         bina=bina*10;
//     }
//     cout<<bin;
// }

// #include<iostream>
// using namespace std;
// int main()
// {
//     int n,a[100],diff=4,i;
//     a[0]=1;
//     cout<<"Enter number of elements\n";
//     cin>>n;
//     for(i=1;i<n;i++)
//     {
//         a[i]=a[i-1]+diff;
//         diff+=5;
//     }
//     cout<<"The series is= ";
//     for(i=0;i<n;i++)
//     {
//         cout<<a[i]<<" ";
//     }
//     return 0;

// }

// #include<iostream>
// using namespace std;
// int main()
// {
//     int a[100],n,i,diff=2;
//     a[0]=1;
//     a[1]=3;
//     cout<<"Enter the value of n";
//     cin>>n;
//     for(i=2;i<n;i++)
//     {
//         a[i]=a[i-1]+diff;
//         diff+=2;
//     }
//     cout<<"The series is= ";
//     for(i=0;i<n;i++)
//     {
//         cout<<a[i]<<" ";
//     }
//     return 0;

// }

// #include<iostream>
// using namespace std;
// int main()
// {
//     int a[100],n,i,diff=3;
//     a[0]=1;
//     cout<<"Enter the value of n\n";
//     cin>>n;
//     for(i=1;i<n;i++)
//     {
//         a[i]=a[i-1]+diff;
//         diff+=8;
//     }
//      cout<<"The series is= ";
//     for(i=0;i<n;i++)
//     {
//         if(i%2!=0)
//         {
//         cout<<a[i]*-1<<" ";
//         }
//         else{
//             cout<<a[i]<<" ";
//         }
//     }
//     return 0;

// }

// #include<iostream>
// using namespace std;
// int main()
// {
//     int n,a[100],i,diff=2,j=1,inc=2;
//     a[0]=6;
//     a[1]=8;
//     cout<<"Enter the value of n\n";
//     cin>>n;
//     for(i=2;i<n;i++)
//     {
//         a[i]=a[i-1]+diff;
//         diff+=inc;
//         inc+=2;
    
//     }
//      for(i=0;i<n;i++)
//     {
//         if(i%2!=0)
//         {
//         cout<<a[i]*-1<<" ";
//         }
//         else{
//             cout<<a[i]<<" ";
//         }
        
//     }
// }

// #include <iostream>
// #include <cstring>
// #include <cmath>
// using namespace std;



// int main() {
//   int N = 100000;

//  int i = 6;
//   int j = 17;
//  int k = 50;
//   int l = 60;

//   while(i <= N)
//  {
//   cout<<i<<", ";

//   i += j;
//   j += k;
//   k += l;
//   l += 24;
//   }

//   return 0;
// }

#include<iostream>
using namespace std;
int main()
{
    int n,i,j,p=1,in=1;
    cout<<"Enter the value of n\n";
    cin>>n;
    for(i=0;i<n;i++)
    {
        for(j=1;j<i+1;j++)
        {
            cout<<p<<" ";
            p=p+in;
            in++;
        }
        cout<<endl;
    }
}