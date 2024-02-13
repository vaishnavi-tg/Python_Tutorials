'''name='Data science masters'
print(name.capitalize())#makes the 1st character capital

#Reversing a string 
print(name[::-1])
print(' '.join('vaishnavi'))
print(' '.join(reversed('vaishnavi')))
print(' dad '.join('Pin'))
print(' dad '.join(reversed('Pin')))
print(str(reversed('ant')))#gives object adress
# convert to list
print(list(reversed('ant')))
for i  in list(reversed(name)):
    print(i,end=' ')'''
# Removing  character from the end of the string 
'''string='        Impact.Datascience        '
print(string.lstrip(' '))#removes the spaces at the left side 

print(string.rstrip(' '))#removes the spaces at the right side 
string_1='Greetings From the Impact batch'
print(string_1.replace('Greetings','Wishes'))
print('hello \t World '.expandtabs())
str_1="Welcome to PW skills . Welcome to dat cience"
print(str_1.replace('dat','data').replace('cience','science'))
print(str_1)
a="the world"
print(a.islower())
ab='VAISHNAVI '
print(ab.isupper())
print(ab.isspace())
print(' '.isspace())
if (' '.isspace()):
    print("Helloworld")

if('vaiSh'.islower()):
    print("Datascience")
else:
    print('???')    


if('VAISHNAVI'.isupper()):
    print("Your gonna be a data scientist")
else:
    print("!!!!!")  


ex='vaishnavi tg'
print(ex.endswith('g'))
print(ex.startswith('v'))

#check if the given string is alphanumeric or not 
string_a='pwskillsisthebestbatch34567'#if spaces  is thier then it shows false
print(string_a.isalnum())

#wap to count the number of characters in the string 


x=input("Enter the string:    ")
count=0
for i in x:
    count=count+1
print("The total number of characters in the given string are ",count)   
print(len(x) )

z='vaishnavi'
for i in z:
    print(i,end=' ')


for i in range(len(z)):
    print(i,'=',z[i])


for i in range(len(z)-1,-1,-1):
    print(z[i])'''



string='pwskills'
ch=len(string)-1
while(ch>=0):
    print(string[ch])
    ch=ch-1

             