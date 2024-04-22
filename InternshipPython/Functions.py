# No parameters no return type
'''def pr():
    for i in range(10):
        print("Hola")
pr()        
pr()
# With parameters without return type 
def a(n):
    for i in range(n,n+10):
        print(i)
a(100)
a(3)

# Overloading a function 
# If name of 2 functions is same then this is the way of order of function being checked 
# Name of function =====parameters ====No. of parameters ====order of parameters 


def sq(n):
    for i in range(n):
        print("*"*n)
sq(5)        
def py(n):
    for i in range(1,n+1):
        print(" "*n-i+"*"*i)

py(5)   '''    



# Function defition:
# using the def statement is the most common way to define a function in py.
# The 
# def function_name(parameters):
# statement(s)
# Function name is the identifier of the function 

'''def atm(withdrawal):
    def bal_enq():
     main_balance=100000
    print("Your main balance is Rs One lakh only: \n",bal_enq)
    def withdrawl(wit_drw):
        n=int(input("Enter the amount that is to be withdrawed"))
        if withdrawl<=bal_enq:
            if (0.1*bal_enq)>=bal_enq-wit_drw:
                print("Your amount is being withdrawed",wit_drw)
                print("Your remaining balance is ", bal_enq-wit_drw)
            else:
                print("You should keep minimun of 10% of your main balance\n")
        else:
            print("Insufficient funds availabel\n")            

    print("Do u want to get the receipt of the transaction\n")
    opt=int(input("Enter Yes or No\n"))
    if(opt=="yes" or 'Yes'):
        rec(withdrawl)
    elif(opt=="No"or"no"):
        print("Thanku you")
    else:
        print("Invalid ...Choose the right option ") 
def rec(withdrawl):
    print("Your receipt for withdrawal\n")
    print("Your remaining balance is ", (bal_enq-withdrawl))
    print("Thanku you visit again !!!")
        
atm(2000)'''



# ATM terminal application
b=0
def m():
    print("Atm menu:")
    print("1.Check balance")
    print("2.Deposit")
    print("3.Withdrawal")
    print("4.Exit")

def c():
    print("Your balance is : $"+str(b))

def d():
    global b 
    a=float(input("Enter the deposite amount:$\n"))
    b+=a
    print("Deposit of $"+str(a)+"successful")
    c()

def w():
    global b
    a=float(input("Enter the withdrawal amount:$\n"))
    if a<=b:
        b-=a
        print("withdrawal of $"+str(a)+"successful...")
    else:
        print("Insufficient balanace")
    c()

def a():
    while True:
        m()
        c=int(input("Enter your choice;\n"))
        if c=='1':
            c() 
        elif c=='2':
            d()  
        elif c=='3':
            w()       
        elif c=='4':
            print("Thank you")
        else:
            exit    
 
m()

    
