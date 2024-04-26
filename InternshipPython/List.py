# List functions usage
'''l=[0,1,2,3,3,4,5,6]
l1=[9,7,8,9,1,2,3,4]
print(l[5])
print(l.append(7))  #Append adds the element at the end of the list 
print(l)
m=l.count(3)#Counts the element that v want to search
print(m)
n=l.clear()#Clears the list
print(n)
# In list slicing dont mention value as the initial and final point ..mention index for strting and ending 
x=l[0:len(l):2]
print(x)
l.sort()#Sorts the list
print(l)
# List reversing 
l.reverse()#Reverses the list 
print(l)
l.extend(l1)#Extends the exsisting list
print(l)
l1.index(3)
print(l1)#Returns the index of the element
l.insert(3,678)
print(l)#Inserts the element at the specified element 
l.pop() #Removes element at the end of the list 
print(l)
l.remove(678)#Removes element wereever want
print(l)

# Adding number to the list as taking the input frm the user \


# Arranging the elements as the input give the input 
l=[]
n=int(input("Enter the no of elements\n"))
for i in range(n):
    #loop vll end at the first element that v give 
    l.append(int(input("Enter the elements\n")))
l.sort()
l.reverse()
print(l)

# Making in string form
l=[]
n=int(input("Enter the no of elements\n"))
for i in range(n):
    #loop vll end at the first element that v give 
    l.append(int(input("Enter the elements\n")))
l.sort()
l.reverse()
op=' '
for i in range(n):
    op+=str(l[i])
print(l)
print(op)'''

# Sum of the first half of the list

'''l=[]
sum=0
n=int(input("Enter the no of elements\n"))
for i in range(n):
    #loop vll end at the first element that v give 
    l.append(int(input("Enter the elements\n")))
l.sort()
l.reverse()
sum=0
for i in range(len(l)//2):
    sum+=l[i]
print(sum)'''

# Even index element sum and odd index element sum 
# Occurances of the element in the list 
'''l=[]
n=int(input("Enter the number of elements\n"))
for i in range(n):
    l.append(int(input("Enter the element\n")))
for i in range(n):
      print(l[i],'is occured for',l.count(l[i]))
print(l)    


# print the unique element ie  Non REPEATING ELEMENT  
l=[]
n=int(input("Enter the numbers\n"))
for i in range(n):
     l.append(int(input()))
print(l)
for i in range(n):
     if(l.count(l[i]==l)):
          print("The non repeating element is ",l[i])    ''' 


# print the not unique element ie  REPEATING ELEMENT  
'''l=[]
n=int(input("Enter the numbers\n"))
for i in range(n):
     l.append(int(input()))
print(l)
for i in range(n):
     if(l.count(l[i]>1)):
       print("The repeating element is ",l[i]) '''   


# Very Important
# Rotational list
def rl(lst,k):#k is rotation number here
    # rl=rotated list
    n=len(lst)
    k=k%n
    return lst[k:]+lst[:k]
lst=input("Enter the list:\n").split()
lst=[int(num)for num in lst]
k=int(input("Enter the number of positions to rotate:"))
rl=rl(lst,k)
print("Original list:",lst)
print("Rotated list:",rl)


# 90 degree rotation of a list
# That is row to column and vice versa
def r90(matrix):
    if not matrix:
        return[]

    r,c=len(matrix),len(matrix[0])
    rotated=[[0]*r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            rotated[j][r-1-i] =matrix[i][j]


    return rotated

    rows=int(input("Enter the rows\n"))
    cols=int(input("Enter the cols\n"))


    m=[]
    for i in range(rows): 
        row=list(map(int,input().split()))
        if len(row)!=cols:
            print("Error")
            break
        m.append(row)  

    rotated=r90(m)


    for row in rotated:
        print("row")
                  
