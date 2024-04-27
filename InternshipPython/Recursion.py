'''def pr(n):
    if n<=100:
        print(n)
    return pr(n+1)
pr(1)   
#Tailed recursion Eg is aabv
#Recursion====Direct and Indirect 
#Direct====Head and Tail recursion
#Head Recursion====A recursive call is made in the  first stmt vthin the function 
#Tail Recursion====A recursion call is made in the last stmt vthin the function  
# In tail Apprach is down to up 
# In Head it is up to down
# Head reursion 
def pr(n):
    if n>0:
        pr(n-1)
        print(n,end=' ')'''


'''def f(n):
    if n>0:
       print(n,end=" ")
        f(n-1)
        f(n-1)
f(3)  '''              
 


def f(k):
    if(k>0):
        res=k+f(k-3)+(k-6)
        print(res)
    else:
        res=0
    return res
f(1)            
        