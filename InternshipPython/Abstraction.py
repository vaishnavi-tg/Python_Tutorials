
# V ll hide certain info frm user that is abstraction 
# Use abstract keyword
# U cant directly use abstarct class, u have to inherit the abstract into some new class and use it 
#u r importing abstaract frm abc as ABC
# To hide info dont define anything in abstract method 
from abc import ABC,abstractmethod
class animal(ABC):
    def __init__(self,name):
        self.name=name
        
    @abstractmethod
    def make_sound(self):
        pass
class Lion(animal):
    def make_sound(self):
        return "Roar!"
class Penguin(animal):
    def make_sound(self):
        return "Honk Honk!" 
class dog(animal):
    def make_sound(self):
        return "Bow Bow" 
class cat(animal):
    def make_sound(self):
        return "Meow Meow"       
l=Lion(animal)
n=l.make_sound()
print(n)
c=cat(animal)
d=c.make_sound()
print(d)



    