# Arithmametic Operators(PEDMAS)
# Precedence for arithematic operators (parenthesis(power),exp,mul,div,add,sub)
n=(10+42*(4+2**2))
print(n)
# If 2 parenthesis solve and keep aside and then go with the next operations
n=(77+52*(3+2**2)-(23+(3**2)))
print(n)
n=(77+52*(3+2**2)//(23+(3**2)))  #Floor division
print(n)
# Comparision operator(2nd priority to arithematic )
n=((77+52*(3+2**2))>560)
print(n)
n=((77+52*(3+2**2))==441)
print(n)
# Bitwise operator
n=(((77+52*(3+2**2))==441)and(456==456))
print(n)
# Not in and in are membership operator
# Logical ------> and or not are the  priorities 

# Bitwise operators
print(bin(524))
# 512 256 128 64 32 16 8 4 2 1 
print(hex(100))
num=((45&32)//((2**4)+2)^35)
print(num)
n=34
print(type(n))
# Operators assositivity
n=(2**3**2)
print(n)
# Membership operator
l=[1,2,3,4,5,6]
print(7 in l )
n=(2+3-4*12/2)
m=4
k=int(n+m)
print(bin(k))


















