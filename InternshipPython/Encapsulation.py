# If u try to wrap any method, object , a varibale within a set of class it is encapsulation 
# No private like that all 
# If u give sumthng in self its like private 
class base:
    def __init__(self):
        self.a=100
        self.b=200
        self.c=300
class derived(base):
    def __init__(self):
            base.__init__(self)#Dunction call of private member
            print("Protected element")
            print(self.a)
            print(self.b)
            print(self.c)
ob2=derived()
ob3=base()  
print(ob2)
print(ob3) 


