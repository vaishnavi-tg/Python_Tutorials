def test():
    pass
def test1():
    print("Hello Good morning Guys")
test1()  
def test2():
 return "Hello Guys we are from BITM"
# test2() +'vaish'
print(test2()  +  'vaish')
def test3():
   print( 1,2,3,'Pw Skills',8)
test3()
print(test3())
def test4():
   a=3*4+5-2
   return(a) 
print(test4())  
def test5():
   return"this is Hi"
print(test5())

def test6():
   return 'skills','3','6'
print(test6())
print(test6()[2])
print(test6()[1])
def test7():
   a=4+5*7
   return a 
(print(type(test7())))
def test8(a,b):
   c=a+b
   return c
print(test8(2,4))
print(test8("vaish","chinna"))
print(test8([1,2,3,4,5],[6,7,8,9,0]))
print(test8(b='navi',a='vaish'))
#Create a function that will take input as a list and return only the numeric values 
list=['vaishu','prathu','kish',1,2,3,4,5,6,[23.45]]
def test9(a):
   n=[]
   for i in a :
      if type(i)==int or type(i)==float: 
         n.append(i) 
   return n
print(test9(list))      
def test10(a):
   n=[]
   for i in a:
      if type(i)==list:
         for j in i :
            if type(j)==int or type(j)==float:
             n.append(i)
            return n

