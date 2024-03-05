'''name=input("enter the name \n")
print(name,"Good afternoon")
print("Good afternoon" + name)'''




name=input("enter your name :\n")
date=input("enter the date : \n")
template='''Dear <|name|>,
Your selected
on the <|date|>'''
print(template.replace('<|name|>',name).replace( '<|date|>',date))

