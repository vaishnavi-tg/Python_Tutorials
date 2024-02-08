s1=input("Enter the string 1")
s2=input("Enter the second string as same as length of string 1")
output=""
i=j=0
while i<len(s1) or j<len(s2):
    output=output+s1[i]+s2[j]
    i=i+1
    j=j+1
print(output)    
