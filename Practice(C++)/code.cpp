// #include<iostream>
// using namespace std;
// int main()
// {
//     int i,n=0,a,b=0;
//     for(i=1;n<4;i++)
//     {
//         b++;
//        a= 7*i;
//         if(a%2==1&&a%3==1&&a%4==1&&a%5==1&&a%6==1)
//         {
//             n++;
//         if(n==3)
//         {
//             continue;
//         }
//         cout<<a<<" ";
//         }
//     }cout<<"iterations= "<<b;
//     return 0;
// }
// #include <iostream>
// using namespace std;



// // Multiple of 7



// int main() {
//  int LCM = 60;
//  int NumTerms = 4;

//  int multiple = 301;
//  int count = 1;

//   int iterations = 0;

//  while(count<=NumTerms)
//   {
//   if(multiple % 7 == 0)
//  {
//   if(count!=3)
//  cout<<multiple<<", ";
//  ++count;
//   }

//   multiple += LCM * 7;

//  ++iterations;
//   }

//  cout<<"\n#Iterations : "<<iterations<<endl;
//   return 0;
// }

// #include <iostream>
// using namespace std;

// // Multiple of 7

// int main() {
//     int LCM = 60;
//     int NumTerms = 4;

//     int multiple = 301;
//     int count = 1;

//     // Calculate the first multiple of 7 greater than or equal to 301
//     multiple = (multiple / 7) * 7;
//     if (multiple < 301) {
//         multiple += 7;
//     }

//     // Print the required multiples of 7
//     for (int i = 0; i < NumTerms; ++i) {
//         if (i != 2) { // Skip the third term
//             cout << multiple << ", ";
//         }
//         multiple += LCM * 7;
//     }

//     cout << "\n#Iterations : 1" << endl;
//     return 0;
// }

// #include<iostream>
// using namespace std;
// int main()
// {
//     float n;
//     int a;
//     float z;
//     cout<<"Enter the value";
//     cin>>n;
//     a=int(n);
//     cout<<a;
//     cout<<n-a;
// }

// #include<iostream>
// using namespace std;
// int main()
// {
//     int a,b,c;
//     cout<<"Enter a ";
//     cin>>a;
//     cout<<"Enter b";
//     cin>>b;
//     a=a+b;
//     b=a-b;
//     a=a-b;
//     cout<<"a= "<<a<<" "<<"b= "<<b;
//     return 0;
// }

// #include<iostream>
// using namespace std;
// int main()
// {
//     int a,b,c;
//     cout<<"Enter the value of a,b,c ";
//     cin>>a>>b>>c;
//     if(a>b&&a>c)
//     {
//         cout<<a<<" is largest\n";
//         if(b>c)
//         {
//             cout<<b<<" is second largest\n";
//         }
//         else{
//             cout<<c<<" is second largest\n";
//         }
//     }
//     else if(b>a&&b>c)
//     {
//         cout<<b<<" is largest\n";
//         if(a>c)
//         {
//             cout<<a<<" is second largest\n";
//         }
//         else{
//             cout<<c<<" is second largest\n";
//         }
//     }
//     else if(c>a&&c>b)
//     {
//         cout<<c<<" is largest\n";
//         if(a>b)
//         {
//             cout<<a<<" is second largest\n";
//         }
//         else{
//             cout<<b<<" is second largest\n";
//         }
//     }
//      else if(a==b&&a==c)
//     {
//         cout<<"All are equal";
//     }
//     else if(a==b||a==c)
//     {

//         cout<<a<<" is largest\n";
//         cout<<c<<" is second largest\n";
//     }
//     else if(b==c||b==a)
//     {
//         cout<<b<<" is largest\n";
//         cout<<a<<" is second largest\n";
//     }
//      L1: else if(c==a||c==b)
//     {
//         cout<<c<<" is largest\n";
//         cout<<b<<" is second largest\n";
//     }
    
// }



#include<iostream>
using namespace std;
int main()
{
    int n,rem;
    cout<<"Enter a number";

}