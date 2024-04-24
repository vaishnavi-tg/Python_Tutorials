# Frozen set:We will get the output in the ordered form only 
h={1,2,3,4,5,6}#same numerals u ll get 
print(h)#in set if u give numerals it v ll print in the same order but if u give string it vll change 
print(type(h))
fs=frozenset(h)#u ll get correct order in frozen set even if u do many times but first time wen u run the code u ll get the jumbled form 
print(fs)
g={'1','2','3','4','5','6'}
print(g)#Here u ll get jumbled 
i={'1','2','3','4','5','6'}
print(frozenset(i))


