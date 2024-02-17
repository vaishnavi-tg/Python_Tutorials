n=2
c=3
def test(n,c):
    return n**c
print(test(2,3))
a=lambda c,b: c**b
print(a(3,2))
add=lambda a,b:a+b
print(add(3,5))

c_to_f=lambda c:  (9/5)*c+32
print(c_to_f(34))


max2=lambda a,b: a if a>b else b
print(max2(9,4))


str="vaishnavi tumbalam gutti "
str_len=lambda s : len(s)

print(str_len('vaishnavi tg'))