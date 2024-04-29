# Print the letters according to the number beside
'''ip=input("Enter the String\n")
c=' '
n=0
res=" "
for i in range(len(ip)):
    if i%2!=0:
      n=int(ip[i])
      res+=c*n
    else:
       n=ip[i]
print(res)   '''    




# String methods
# Vowel and consonants seperation
'''str=input("Enter the word or a sentence\n")
vowels=' '
consonants=' '
v='aeiouAEIOU'
for i in range(0,len(str)):
   if str[i] in v:
      vowels=vowels+str[i]
   else:
      consonants=consonants+str[i]
print("The consonants in the given sentence are:",consonants)
print("The vowels in the given word are:",vowels)


# Case changing in string 
# lower():All to lower 
# upper():All to upper
# title():coverts all to bold
# swapcase():swaps upper to lower and viceversa
# caplitalize():convert the first character of a string to uppercase
# casefold():implements caseless string matching
# center():pad the string with the specified character
# count():return the number of occurances of a substring in the string 
# encode():encodes strings with the specified encoded scheme 
# expandtabs():specifies the amount of space to be submitted with the "\t" symbol in the string
# find():returns the lowest index of the substring if it is found
# format():formats the string for printing it to console 
# format_map():formats specified values in a string using a dictionary 
# index():returns the position of the first occurance of a substring in string 
# isalnum():checks if all the characters in a given string is alphanumeric or not 
# isalpha():Returns"True"if all characters in the string are alphabets
# isdecimal():Returns"True"if all characters in the string are decimal
# isdigit():Returns"True"if all characters in the string are digit
# isidentifier():checks if the string is valid identifier or not
# isnumeric():Returns"True"if all characters in the string are numeric characters
# isprintable(): Returns"True"if all characters in the string are printable or the string is empty
# isspace():Returns"True"if all characters in the string are whitespace charcters
# istitle():Returns'True' if the string is a titile cased string
# join():Returns a concatenated string
# ljust():Left alings the string accorsing to the width specified
# lstrip():Returns the string with leading characters removed
# maketrans():Returns a translation table
# partition():splits the string at the first occurance of the seperator
# replace():Replaces all the occurances of a substring with other substring
# rfind():Returns the highest index of the substring
# rindex():Returns the highest index of the substring inside the string 
# rjust():Right alings the string accorsing to the width specified
# rpartition():Splits the given string into 3 parts
# rsplit():split the string from the right by the specified seperator 
# splitlines():split the lines at the line  boundaries
# rstrip:Removes trailing charcater
# startswith():Returns "True "if a string starts with the given prefix
# strip():Returns the string with both leading and trailing characters 
# translate():modify string according to given translation mapping
# zfill():Returns a copy of the string with '0'characters padded to the left side of the string 
 

# String Functions

str="Geeks for geeks"
print(str.lower())
print(str.capitalize())
print(str.swapcase())
print(str.casefold())
print(str.center(4))
print(str.title())



# Toggling alphabets cases
print(ord('H')^32) 
# Using functions


def toggling(ip):
   res=" "
   for i in range(0,len(ip)):
      c=chr(ord(ip[i])^32)
      res=res+c
   return res
   
ip=input("Enter the sentence\n")
res=toggling(ip)
print(res)'''



# String slicing 
s=" Ballari Institute of Technology and Management"
print(s[0:5])
print(s[0:15:2])


# Reversed of the string
print(s[len(s)-1:0:-1])

#n="beauty"
#print(n[6:1:-1])


def ab(s):
 c=0
res=" "
for i in range(len(s)):
   for j in range(i+1,len(s)+1):
      res=res+s[i:j]
      print(res)
      res=""
      c=c+1
   print(c)
ab("folk")     

      


ip=str (input())
x=len(ip)
for i in range(x):
 for j in range(x):
   if (i==j or i==x-1-j):
       print(ip[i],end=" ")
   else:
        print("  ",end=" ")                     
print(" ")   


def x(s):
 n=len(s)
for i in range(n):
   for j in range(n):
      if (i==j or i+j==n-1):
         print(s[i],end=" ")
      else:
         print(" ",end=" ")
   print()          

s=input()
x(s)