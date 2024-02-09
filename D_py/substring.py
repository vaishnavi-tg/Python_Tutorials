str=input("Enter the string : ")
subs=input("Enter the substring :")
s=str.split(",")
print(s)
list=list(s)
list1=len(list)
for i in range(0,list1):
    if i==subs:
        print("Substring found at the position",i, "and the substring is",subs)
    else:
        print("Substring not found in the string")    

