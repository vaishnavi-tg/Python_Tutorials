import random

def swg(comp,mine):
    if(comp==mine):
        return None
    if(comp=='s' and mine=='g'):
        return True
    elif(comp=='w' and mine=='s'):
        return True
    elif(comp=='g' and mine=='w'):
        return True
    else:
        return False
    
choice=["s","w","g"]
comp=random.randint(0,2)
comp=choice[comp]
mine=(input("Choose either s,w,g   :"))

win=swg(comp,mine) 
if win is None:
    print("Match is draw")
if win:
    print("You won")
else:
    print(f"You choose {mine} and the computer chose {comp} ")
print("You loose")

