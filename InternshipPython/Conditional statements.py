'''if 10==2:
    print('y')
else:
    print('n')    

if print('qwerty'):#otherthan True watever prints it false in py
    print('y')
else:
    print('x')    

if (-345):
    print("True")
else:
    print("False")   
#coz anything other than 0 is True 
#wap to determine whether the password is ri8 or no 
# conditions:Check if starting letter is capital 65 to 90
# Str lenght shud be 8 letter of minimun 
n=input("Enter the password \n")
c=ord(n[0])
k=len(n)
if ((c>=65&c<=90)&(k>=8)):
    print("You have made a strong password")
else:
    print("You do not have a strong password") '''   
'''year=int(input("Enter the year\n"))
if((year%400==0 )or (year%100!=0 )) and (year%4==0):
    print("Its a leap year")
else:
    print("Its not a leap year")  '''      

'''num=int(input("Enter the number \n"))
if((num==0) or (num==1) or (num==3) or (num==5) or (num==6)or (num==9)):
   print("You are allowed ") 
else:
   print("your not allowed") '''  
# Gradings system 
marks=int(input("Enter the marks \n"))
if (marks>=90 and marks<=100):
   print("A+")
elif(marks<=90 and marks>=80):
    print("A")   
elif(marks<=80 and marks>=70):
    print("B+")   
elif(marks<=70 and marks>=60):
    print("B")  
elif(marks<=60 and  marks>=50):
    print("C+")   
elif(marks<=50 and marks>=40):
    print("C")   
elif(marks<=0 and marks>100):
    print("Enter the marks within the specified range") 
else:
    print("F")    
    
# Atm 
'''amount=int(input("Enter the total amount \n"))
withdrawal=int(input("Enter the amount u want to withdraw \n"))
if(amount>withdrawal):
    if((amount-withdrawal)>=amount*0.1):
        print("You can withdraw your amount")
        print("The remaining balance is ",amount-withdrawal)
    else:
        print("It is mandatory to have a minimum balance ")
else: 
    print("You have insufficient balance")'''              





                          