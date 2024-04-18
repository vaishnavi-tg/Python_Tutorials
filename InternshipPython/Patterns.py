#Palindrome number
n=int(input("enter the number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("its palindrome")
else:
    print("it's nt palindrome")

#Neon number
num=int(input("enter the number"))
sq=num*num
sum=0
while sq>0:
    sum=sum+sq%10
    sq=sq//10
if(num==sum):
    print("its a neon numb")
else:
    print("not neon") 
    
#Pattern
x=int(input())
for i in range(x):
    for j in range(x): 
        print('*',end='')
        
x=int(input())
for i in range(1,x+1):
   for j in range(1,x+1):
       print(j,end=" ")
       print("\n")

#Hallow right angle triangle   
n=int(input()) 
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j:
            
#Alphabet series
x=int(input("enter the number\n"))
count=0
for i in range(x):
    for j in range(x):
        print(chr(65+count),end='')
        count+=1
    print('\n')
    
#Diamond
n=int(input())
for i in range(1,n+1):
    print(" " * (n-i) +"* " * i)
for i in range(n-1,0, -1):
    print(" "* (n-i)+"* " * i)

#Triangle with stars
n=int(input())
for i in range(1,n+1):
    print(" "(n-i)+" "*i) 