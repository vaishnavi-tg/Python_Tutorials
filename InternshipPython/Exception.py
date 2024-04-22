# Error cant be rectified 
# Exception can be rectified 
# 2 types of exception
# Differences
# 1.Runtime: 
# 2.compiletime:
# Types of Errors
# Syntax Errors:Wen syntax dont match
# Type error:Wen try to match int and string 
# Name error:Wen u use keywords as name 
# Index error :wen u use indexes and its out of range
# key error:Wen u give mismatch key then this error 
# Attribute Exception:
# I/O Exception:
# Zero division Exception:
# Import Exception
# To overcome the exception :


# Zero Divison Error
'''n=int(input("Enter the number\n"))
try:
   num=n/0
   print(num)
except ZeroDivisionError:
   print("Zero Division error")  ''' 



# Take multiple except blocks and get the ri8 answer This if for import Error
# Zero Division Error
n=int(input("Enter the number\n"))
try:
    num=n/0
    print(num)
except ZeroDivisionError:
   print("Zero Divison Error")
except NameError: 
   print("Name Error")
except ImportError:
   print("ImportError")
except SyntaxError :
   print("Syntax Error")           


# Import Error
n=int(input("Enter the number\n"))
try:
    import rtyui
except ZeroDivisionError:
   print("Zero Divison Error")
except NameError: 
   print("Name Error")
except ImportError:
   print("ImportError")
except SyntaxError :
   print("Syntax Error")    

# 
