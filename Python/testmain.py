num1=10
num2="a"
try:
    result=num1/num2
except TypeError:
    print("Type Error")
except ZeroDivisionError:
    print("Cannot divide by 0")
else:
    print("The results=",result)
finally:
    print("Done")