
import math

def Fact(n):
    return math.factorial(int(n))
result=Fact(8)
print(f"THe factorial of is: {result}")


a=int(input("Enter the value of A: "))
b=int(input("Enter the value of B: "))
sum=a+b
print(sum)
 
c=int(input("Enter the value of c: "))
d=int(input("Enter the value of d: "))
Sub=c-d;
print(Sub)

factor=int(input("Enter the value you want to perform factorial: "))
def factorial(n):
    result=1
    for i in range (1,n+1):
        result=result*i;
       
    return result
print(factorial(factor))