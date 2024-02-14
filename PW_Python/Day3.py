# Logical operators
# And or not
'''print(True and True)
print(True or True)
print(not True)
print(not(True))
print(not int((bool(0))))
print(  not int(bool(1)))
print(not 0)
print(not 1)
print(not(1000))'''



# Equality operators
'''lst_a=[1,2,3,4,5]
lst_b=[1,2,3,4,5]
print(lst_a==lst_b)
print(lst_a is lst_b)
print(id(lst_a))
print(id(lst_b))'''
'''lst_a=[1,2,3,4,5]
lst_b=[1,2,3,4,5]
print(lst_a is not lst_b)



a=2
b=2
print(id(a))
print(id(b))

s1='vaish'
s2='vaish'
print(id(s1))
print(id(s2))


# Comparision operators

max_bike=150
max_car=200
print(f'The bike speed is greater than the speed of the car :{max_bike>max_car}')
print(f'The bike speed is greater than the speed of the car :{max_bike<max_car}')
# Arithmatic operators
a=15
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)    #dispalys the remainder 
print(a//b)

# Bitwise operators
var=10
print(bin(var))
print(hex(var))
print(~(var))# Its the twos complement 
print(True&False)
print(True|False)
print(var >>1)
print(var <<1)




# Strings

str="Welcome to the Python world"
print(type(str) )
print(str[2])
# str[2]='u'
print(str)
str="vaishnavi TG"
print(str)
print(str.capitalize)




string=("this is the Full stack Data science masters batch")
print(string[5:])
print(string[5])
# print(string[5:11])  String Slicing
print(string[5:11:2])
print(string[5: :-1])
print(string[-2])
print(string[-1])
print(string[-12:-3])
name="Prathyarthi Kashyap"
print(name[-6])
print(name[-2:-5])
print(name[-3:4])
print(name[5:2])
print(name[-3:4])
print(name[-1:-19])
print(name[:])
print(name)
print(name[::])
print(name[::-1])
print(name[::-2])
name='vaishnavi'
print(name[::-1])
print(name[::-2])
print(name[::-3])
print(name[2:9:-1])
course_name='Data science masters'
print(course_name[5:12:1])
print(course_name[-9:-16:-1])
print(course_name[11:4:-1])
print(course_name+'  course')#string concatination 
print(course_name[11:4:1])
print(course_name[11:4:-1])
#string concatination 
print('Hello'+'World')
print(course_name  * 6)
print(len(course_name))
print(course_name.find('n'))#finds the index of the element 
print(course_name)
print(course_name.find('D'))
print(course_name.find('a',2,5))
print(course_name.find('z'))#returns -1 if the element is not present 
#count#gives the count of the element present in that word
print(course_name.count('a'))
print(course_name.count(' '))
print(course_name.count('    '))
print(course_name.count(''))#it means that it counts every character in the given sentence
#count and length should be same becoz they count every character 
print(course_name.count('Data'))
print(course_name.count('D')) 



#string split function         Removes the element specified     Here the element is gone 
print(course_name.split(' '))
print(course_name.split('s'))


#string partition function     brings back the specified element 

print(course_name.partition('a'))'''





# String uppercase and lower case

'''print(course_name.upper())
print(course_name.lower())
print(course_name.swapcase())#converts upper to lower and VV
#title case      Every word first letter will be in capital
print(course_name)
print(course_name.title()) 

name='lakshmi narayan'
print(name.title())'''



name=input("Enter the name      ")
vowels='aeiouAEIOU'
for ch  in name:
    if ch in vowels:
        print("{} is a vowel".format(ch))
    else:
        print("{} is is a consonant".format(ch))       
