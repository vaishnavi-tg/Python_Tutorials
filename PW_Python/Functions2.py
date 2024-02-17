def test():
    pass
test()
def test1(a,b,c):
    return a,b,c
print(test1(2,3,4))
def test2(*args):
    return args
print(test2(1))
print(test2(1,2,3,4,5,6,7,8,9))
print(test2(1,2,3,4,5,6,7,8,9,[1,2,3,4],(34,56,78),{1,2,3,4,5}))
def test3(*args,a):
    return args,a
print(test3(1,2,3,4,5,a='Vaishnavi'))
def test4(*args):
    l=[]
    for i in args:
        if type(i)==list:
            l.append(i)
            return l
print(test4(1,2,3,[3,4,5],(2,3,4)))
def test5(**kwargs):
    return kwargs
print(test5())
print(type(test5()))
print(test5(a=67,b=23.44,c="vaishnavi TG"))
def test5(*args,**kwargs):
    return args,kwargs
print(test5(4,'vaishnavi',a='apple',b='banana',c='carrot'))


    




