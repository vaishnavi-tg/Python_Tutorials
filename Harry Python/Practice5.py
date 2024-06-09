'''a=int(input("enter the first number  :   "))
b=int(input("enter the second number :   "))
c=int(input("enter the third number  :   "))
d=int(input("enter the fourth number :   "))
if(a>b):
    maxnum1=a
elif(b>a):
     maxnum1=b
if  (c>d):
     maxnum2=c
elif(d>c):
     maxnum2=d
if(maxnum1>maxnum2):
     print( "This is the greatest of the given four numbers", maxnum1)
else:
     print("This is the greatest of the given four numbers",maxnum2)   ''' 




'''m1=int(input("enter the marks of the subject 1:     "))
m2=int(input("enter the marks of the subject 2:     "))
m3=int(input("enter the marks of the subject 3:     "))
avg=(m1+m2+m3)/3
if(avg>=40):
    if(m1>=33 and m2>=33 and m3>=33):
     print("Congratulations you are passed the exam")
else:
    print("Sorry your not passed ")'''







'''spamwords=["make a lot of money","buy now","subscribe this","click this"]
msg="make a lot of money "
spam=False
if('make a lot of money' in msg):
       spam=True
if('buy now' in msg):
       spam=True
if('subscribe this 'in msg):
       spam=True
if("click this" in msg):
     spam=True
print("spam is ", spam)  '''




'''name=input("Enter the username    :")
len(name)
if(len(name)>=10):
    print("username has 10 letters")
else:
    print("username is less than 10 letters")'''



'''l=["chinnu","chinni","cutie","cutipie"]
name=input("Enter the name   :")
if(name in l):
    print("The name is available in the given list",name)
else:
    print("The name",name,"is not availabel")'''





'''marks=int(input("Enter the total marks obtained by the student:    "))
if(marks>=90 and marks<=100):
    print("Excellent")
elif(marks>=80 and marks<=90):
    print("A")
elif(marks>=70 and marks<=80):
    print("B")
elif(marks>=60 and marks<=70):
    print("C")
elif(marks>=50 and marks<=60):
    print("D")
else:
 print("F")   '''


text=input("Enter the text:   ")
if 'valid' in text.lower():
   print("valid is availabel")
else:
   print(" valid isNot availabel ")    
 



    

