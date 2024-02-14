#Types of print statement
'''print("vaishnavi")
age=56
print("My age is:",age)
print(f"My age is :{age}")#fstring
#format string 
name='vaishnavi'
company='Atlassian'
print('My name is {} and my company is {}'.format(name,company))
#place holder
print("My name is {fname} and my company is {fcompany}".format(fname=name,fcompany=company))
#Assignment 
name='vaishnavi'
age=19
degree=BE

My name is vaishnavi my age is 19  and degree is BE '''
#Use fstring and .format  
'''name="vaishnavi"
age="19"
degree='BE'
print(f"My name is {name} and my age is {age} and my degree is {degree}")
print("My name is {fname} and my age is {fage} and my degree is {fdegree}".format(fname=name,fage=age,fdegree=degree))
#control Flow
#Decision making statements
age=int(input("Enter the age of the person  :   "))
if age>=18 :
    print("you are eligible to vote")
else:
    print("You are not eligible to vote")
#Run time input
age=int(input("Enter the age  :  "))
print(type(age))
#task
age=int(input("enter the age :  "))
if(age>=18 and age<=45):
    print("You are young blood")
else:
    print("Thank you we will let you know")  

#task 2
# mall
# product>1000===20%off
# print the price of the product
# product<1000====30%off 
# print the price  of the product      
price=int(input("Enter the price of the product:  "))
if price>1000:
    dprice=(20/100)*price
    print("The discount price of the product is :",dprice)
    print("you are supposed to pay",price-dprice)
elif price<1000:
    dprice=(30/100)*price
    print("The discount price of the product is :",dprice)   
    print("you are supposed to pay ",price-dprice) '''

#more condition 
#mal.....
# if price >3000  /20%off
# if price >=2000 and <=3000  /30%off
#if price >=2000 and <=1000   /40%off


'''price=int(input("enter the price of the product :   "))
if (price>3000):
    if (price==4000):
         print(" COngratulations you won a trip to goa")
    dprice=(20/100)*price
    print(f'The disount price is {dprice} and the amount that is to be paid is {price-dprice}')
elif(price>=2000 and price<=3000):
        if(price==2999):
             print("You have additional gift")
        dprice=(30/100)*price
        print(f'The discout price is {dprice} and the amount that is to be paid is{price -dprice}')
        
elif(price>=100 and price<2000):
    dprice=(40/100)*price
    print(f'The discount price is {dprice} and the amount that is to be paid is {price-dprice}')
else:
     print("Lets drink the tea")  
     print ("I ll be with you")  

#single statements suites
val=int(input("enter the value :  "))
if(val>=688):print("Value is greater than 688")
else:
      print("Kuch nai")

#Loops 
#for loop
#while loop
# nested loops
# loop control (break,continue,pass)



# While -else
joining_age=25
while(joining_age<=60):
     joining_age=joining_age+1
     print(joining_age)
else:
     print("Its time for retirement ")     


#Atm machine
total_amount=1000
while(total_amount!=0):
     total_amount=total_amount-100
     print(total_amount)
else:
     print("Your balance has reached to the end") 
print(Hello all )'''


# For loop
      
lst=['apple',1,2,3.56,True,'s']
print(type(lst))
print(lst[0])
print(lst[4])
for i in lst:
    print(i)
print("The list is empty now ")  

# Output in same line
fruits_list=['mango',"banana",'orange','kiwi','grapes']
for i in fruits_list:
    print(i,end='  ')
    if (i=='orange'):
     print("The fruiit is orange",end='  ')

# Output in new line
fruits_list=['mango',"banana",'orange','kiwi','grapes']
for i in fruits_list:
    print(i)
    if (i=='orange'):
     print("The fruiit is orange")     


fruit='musk melon'
for i in fruit:
   print(i)   


fruit='musk melon'
for i in fruit:
   print(i,end='  ')      

print(fruit[1])   



# Nested loops

# range
for i in range(1,10,3):
   print(i)


'''n=5
for i in range(0,n):
   for j in range(0,i+1):
      print("*", end=' ')
   print("\r") ''' 

'''for i in range(0,5):
   for j in range(5-i,5):
      print("*",end=" ")'''



# Loop controls
# Break and continue
'''fruits_list=['mango','banana','orange','pineapple','kiwi']
for i in fruits_list:
   if i=="pineapple":
      break
   print(i)'''



fruits_list=['mango','banana','orange','pineapple','kiwi']
for i in fruits_list:
   if i=="pineapple":
      continue
   print(i)   
 



fruits_list=['mango','banana','orange','pineapple','kiwi']
for i in fruits_list:
   if i=="pineapple":
      pass
   print(i)    