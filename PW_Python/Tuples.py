t=()
print(type(t))
t1=(21,21.3,45.6,'vaishnavi',True,{1,2},4+6j)
print(t1)
print(type(t1))
l=[1,2,3,4,5]
print(type(l))
print(t1)
print(t1[3])
print(t1[6])
print(t1[2])
print(t1.count(3))
print(t1.index('vaishnavi'))
print(t1.index(1))
print(t1[2])
# print(t1[0]=78.3)
print(l[0]==45)
print(t1)
for i in t1:
    print (i     ,type(i))
t2=(1,2,3,4,5)
print(t2*5)    #same is applicable even with string and list 
print(max(t2))
print(min(t2))#tuple is immutable becoz it dosent allow us to change an element at any point 
t1=(1,2,3,4,6)
t2=(4,6,7,8,9)
t3=(t1,t2)
print(t3)
t4=((1,2,3,4),[4,5,6,7])
print(t4)
# update and insert is not posssile in tuples 
# deleting is possible in tuple
del(t4)
# print(t4)
print(len(t3))
# To check if the element is in tuple 
print("vaish" in t3)
print(7 in t2)
a=input("Enter the Name     ")
for i in a:
    print(i,end=' ')