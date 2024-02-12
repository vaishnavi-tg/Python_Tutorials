#Write a Python program that acts as a simple calculator.
# Prompt the user to enter two numbers and an operator (+, -, *, /), and
# then perform the corresponding calculation. Display the result.

num1=int(input("Enter the first number\n"))
operator=input("ENter the operator + ,-,*,/,//\n")
num2=int(input("ENter the second number\n"))
if operator=="+":
    res=num1+num2
elif operator=="-":
    res=num1-num2
elif operator=="*":
    res=num1*num2 
elif operator=="/":
    res=num1/num2
else:
    res="Invalid Operator"

print(f"Result={res}")        
