'''for i in range(1,10):
    print(i)'''

def test2(*args):
  n=[]
  for i in args:
     if type(i)==int :
        n.append(i)
  return n

print(test2(1,2,'v',56.78,33,56))   



# Fibonacci
# 0,1,1,2,3,5,8,13,21,34.....
def test_fib(n):
   a,b=0,1
   for i in range(n):
      yield a 
      a,b=b,a+b

print(test_fib(10))     
for i in test_fib(10):
   print(i)



   