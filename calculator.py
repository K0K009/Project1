ip=int(input("Choose your selection: \n 1. Addition\n2. Subtraction\n Enter your selection: \n"))
num1=int(input("Enter 1st No: "))
num2=int(input("Enter 2nd No: "))

if ip==1:
 add = (num1 + num2)
 print(f"Result = {add}")
elif ip==2:
 sub = abs(num1 - num2)
 print(f"Result = {sub}")