'''i=0
for i in range(0,101):
    print(i)
# Multiples of 3 and 5 but not 10
i=0
for i in range(0,100):
    if((i%3==0 or i%5==0) and (i%10!=0)):
       print(i)
# Using the step function 
i=0       
for i in range(0,5000,100):
    print(i) 
# Reverse using step function 
for i in range(0,101,-1):
    print(i) 
# Even number using step function for i in range(1,100,3):
for i in range(0,101,2):
        print(i)
# Odd number using step function 
for i in range(1,101,2):
     print(i)      
#Fibonaci series
num=int(input("Enter the number \n"))
a=0
b=1
print(a)
print(b)
for i in range(num-2):
    c=a+b
    print(c)
    a,b=b,c

n=int(input("Enter the number \n"))  
for i in range(0,21):
     print(n,'*',i,'=',n*i)         
# Missing number in the sequence 
n=str(input())
ts=45
s=0
for c in n:
     if c.isdigit():
          s=s+int(c)
print(ts-s)  '''       



# Take input in single line and swap the given values 
'''x,y=input("Enter the number\n").split(',')
print(y,x)

# Swap 2 numbers 
x,y=input("Enter two numbers\n").split(',')
x,y=int(x),int(y)
x=x+y
y=x-y
x=x-y
print(x,y)




x,y=input("Enter two numbers \n").split(',')
x,y=int(x),int(y)
x=x*y
y=x/y
x=x/y
print(x,y)'''
# Printing the sequeence of 0 and 1
'''num=int(input("Enter the number\n"))
for i in range(num):
    print(i%2)

# Even and odd count within the specified range
num=int(input("Enter the number \n"))
i=0
evencount=0
oddcount=0
for i in range(num):
    if(i%2==0):
        evencount+=1
    else:
        oddcount+=1
print("The count of even number is",evencount)
print("The count of odd number is ",oddcount)            

# To print the given format 
num=int(input("Enter the number\n"))
for i in range(num):
    print(i,'%','2','=',i%2)


# Find the multiples in the specified of the given number 

num=int(input("Enter the multiple number\n"))
ran=int(input("Enter the range for the multiples to be found\n"))
count=0
for i in range(ran):
    if(i%num==0):
        count+=1
print("The number of multiples of ",num,"in the given range are:",count)  '''  


# Check if the number is divisible by 10 then dont print else print all its factors
'''x=int(input())
for i in range(x+1):
    if(i%2==0):
        print(i)
        if(i%10==0):
            break




        # WHILE Loop 
x=int(input("Enter the present weight\n"))
while x>75:
    print(x)
    x=x-1'''


# print numbers frm 1 to 100 using while loop 

'''i=0
while(i<=100):
    print(i)
    i+=1
 
#Sum of the given digits in a number 
x=int(input("Enter the number "))
c=0
rem=0
while x>0:
    rem=x%10
    c=c+rem
    x=x//10
print(c)

#Count of the given digits in a number 
x=int(input("Enter the number "))
c=0
rem=0
while x>0:
    rem=x%10
    c=c+1
    x=x//10
print(c)'''


# The easiest logic 
# Sum of digits till single  digit 
# If the given number is multiple of nine then sum of digit is also 9 it self for any multiple of nine 
'''x=int(input("Enter the number that is to be added till the last digit\n"))
if (x%9==0):
    print(9)
else:
    print(x%9)'''  


'''num=456
print(bin(num))'''


# Number conversions 
# Decimal to binary 
'''x=int(input("Enter the number to be converted \n"))
rem=0
binstr=""
while x>0:
    rem=x%2
    binstr=str(rem)+binstr
    x=x//2
print(binstr)'''


# Decimal to binary 
'''x=int(input("Enter the number to be converted \n"))
rem=0
binstr=""
while x>0:
    rem=x%8
    binstr=str(rem)+binstr
    x=x//8
print(binstr)   

# For reverse conversion do multiplication ....
# To find number of zeros and ones in a rem
x=int(input("Enter the number to be converted \n"))
rem=0
binstr=""
while x>0:
    rem=x%2
    binstr=str(rem)+binstr
    x=x//2
print(binstr)  
zerocount=0 
onecount=0
for i in binstr:
    if (i=='0'):
        zerocount+=1
    else:
        onecount+=1 
print("The count of zeros in remainder is",zerocount)   
print("The count of ones in remainder is",onecount)   ''' 



# Number conversions are important
 
# Armstrong number :Its a number that is equal to the sum of its own digits
# raised to the power of the number of digits 
x=int(input("Enter the number \n "))
y=x
z=x
cd=len(str(x))
rem=0
sum=0
while z>0:
    rem=z%10
    sum=rem**cd+sum
    z=z//10
if(sum==x):
        print("Its a armstrong number")
else:
        print("Its not a armstrong number")    
#153 


# Palindrome without using inbuilt function
num=int(input("Enter the number that u want to make it as a palindrome \n"))
temp=num
rev=0
while (num>0):
    n=num%10
    rev=rev*10+n
    num=num//10 
if(temp==rev):
    print("Its palindrome")
else:
    print("Its not a palindrome")

#Neon number 
# Number where the sum of digits of square of the number is equal to the number 
num=int(input('Enter the number\n'))
sqr=num*num
sum=0
while sqr>0:
     sum=sum+sqr%10
     sqr=sqr//10
if(num==sum):
     print("Its a Neon number") 
else:
     print("Its not a Neon Number")         
# 9


#  Palindrome without using inbuilt function
n=int(input("Enter the number that u want to make it as a palindrome \n"))
temp=n
rev=0
while (n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10 
if(temp==rev):
 print("Its palindrome")
else:
 print("Its not a palindrome")
        









