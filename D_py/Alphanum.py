s=input("Enter the string that contains alphabets and numericals\n")
s1=s2=output=" "
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
#To get the sorted as output
for x in sorted(s1):
  output=output+x      
for x in sorted(s2):
    output=output+x
print("The alphabets and numericals availabel in the given string are",output) 
   
