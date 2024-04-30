class you :
    def father(self):
        print("Father and son /daughter")
class mother:
    def father(self):
        print('Husband')
class uncle:
    def father(self) :
        print("Brotherhood")
class stranger:
    def father(self):
        print("stranger")

class grandma:
    def father(self):
        print("son")
                  
y=you()
m=mother()
u=uncle()
s=stranger()
g=grandma()
print(y.father())
print(m.father())
print(u.father())
print(s.father())
print(g.father())





# Method Overloading
# Checks name ,No. of parameter ,Type of paramater
class add:
    def add(self):
        return 0
    def add(self,a,b):
        print(a+b)
        
ad=add()
m=ad.add("erty","werty")
print(m)




# Methos overriding 
class Friend():
    def __init__(self):
        self.value = "3 lakh"
        
    def sh(self):
        print(self.value)

class You(Friend):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.value = "Himalayan bike"
        
    def sh(self):
        print(self.value)

        

fr = Friend()
y = You()
fr.sh()  # Output: 3 lakh
y.sh()   # Output: Himalayan bike


# super(Suppose u have 2 or 3 classes then u want to get the first value apart frm the value tht is given recently
# then use it )

