# def fibonacci(i):
#     if i<=1:
#         return i
#     else:
#         return fibonacci(i-1)+fibonacci(i-2)
# n=int(input("Enter the a number"))
# print("Fibonacci Series is:")
# for i in range(n):
#     print(fibonacci(i), end = " ")
    
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
i=int(input("Enter the a number:"))
if(i<0):
    print("Please enter a postive number!")
else:
    print("Fibonacci Nth number is:",fibonacci(i))