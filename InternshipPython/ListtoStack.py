'''List to stack 
FILO  (Order of stack)
LIFO 
Overflow ----for push check underflow operation stack or not 
condition for underflow----ToP >-1
Underflow(Stack is full)------for pop operation  check overflow 
If stack is full then len-1 index it vll be 
If stack is empty then it v ll be in -1
To print the last added element then condtion is ----print(List(top))
Wen the stack is empty v can push the element 
To access the element of list u can use list index
If u want to access any element in list then u shud access through TOP only 
Underflow---stack is empty 
overflow---stack is full
Push ---adds the element 
pop---removes tthe element 
peak ---prints the last added element 
stack is unidirectional i.e one way 
stack order means reverse order ----coz stack removes frm LAST so print also frm last
overflow condition vll never occur in stack 
'''
#Develop a stack 

class stack:
    # To make a stack v need list so define it 
    def __init__(self):
        self.items=[]
        #To make push function
    def is_empty(self):#is empty deterrmines the given stack is empty or not 
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)               
    



if __name__=="__main__":
    s=stack()
    s.push(2)
    s.push(4)
    s.push(6)
    print(s)
    print(s.items)
    print(s.pop())
    print(s.items)
    print(s.pop())
    print(s.pop())
    s.pop()
    
    

















