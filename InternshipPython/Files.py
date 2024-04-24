import os #All file handling functions are present in os module nly ie remove , close 
f=open("folk.txt","w")
print(f.write("Hello this is internship done by MR.Folk"))
f.close()


import os
f=open("folk.txt",'r')
print(f.read())
f.close()
os.remove("folk.txt")


#OS module functions and its functionality 
#Abort():breaks the file 

f=open("Vaish.txt","w")
print(f.write("Hello Guys This is a anonymous file\n"))
print(f.readable())
print(f.writable())
f.close()

f=open("vaish.txt",'a')
f.write("Hlo Guys v gotta know whos the aynonymous")
f=open("vaish.txt","r")
print(f.read())
f.close()