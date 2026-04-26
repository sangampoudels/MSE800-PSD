def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b


a= float(input("Enter first number:"))
b=float(input("Enter second number:"))
output=input("choose (+, -, *): ")

if output == '+':
   print("Result:", add(a,b))
elif output == '-':
 print("Result:", sub(a,b))
elif output == '*':
 print("Result:", mul (a,b))
else:
 print("Invalid operation")
 