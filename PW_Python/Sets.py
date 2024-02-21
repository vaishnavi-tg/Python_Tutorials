# Always holds unique elements 
s={}
print(type(s))
s1={1,2,3,4}
print(type(s1))
s3={1,2,3,4,5,5,5,67,76,77,7,7,7,7,7,7,8,9,8,8,8}
print(s3)
#say u have a list but u dont want any duplicates then u can convert to a set
a=print(list(s3))
# set cant store list it can store tuples instead becoz it is immutable and set only want to producce unique objects not duplicates
# eg's
s4={1,2,3,4,5,(1,2,3,4,5)}
print(s4)
# s5={1,2,3,4,5,[1,2,3,4,5]}
# print(s5)
s6={1,2,3,'vaish',"Vaish"}
print(s6)
s7={1,2,3,'vaish','vaish'}
print(s7)
#s7[0]#cant becoz it stores hashebly
#s7[1:2:-1]#with indexes v cant access so access with for loop 
for i in s7:
    print(i)
a=s7.add(90)
print(s7)
print(s7.add(2))
print(s7)
print(len(s7))
print(s7)
print(s7.pop())#removes the element 
print(s7)
print(s7.pop())
print(s7.pop())
print(s7.pop())
print(s7)
print(s7.clear())
print(s7)
s8={1,2,3,4,5}
s9={1,2,3,4,6}
print(s8.difference(s9))
print(s9.difference(s8))