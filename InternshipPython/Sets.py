# Set is immutabale,Its unordered collection of sequence with unique collections
s={1,1,2,2,2,9,3,3}
print(s)
# U can use set too find unique elements
# Set is unordered 
# Methods in a set 
s1={1,2,3,4,"1,2,3","vaish"}
s2={2,3,4,5,6,"1,2,3","vaish"}
print(s1-s2)
print(s2-s1)
# For addition v have union function 
# For subtraction v have difference 
b=s1.union(s2)
print(b)
c=s1.difference(s2)
print(c)
d=s1.intersection(s2)
print(d)
e=s1.isdisjoint(s2)
print(e)
# isdisjoint 
f=s1.issubset(s2)#all in s1 shud be in s2
print(f)
g=s1.issuperset(s2)#all s2 shud be present in s1
print(g)

# Print the elements that are same in both the sets
l1=list(input("ENter the first list\n"))
l2=list(input("ENter the second list\n"))
s1=set(l1)
s2=set(l2)
s=s1.intersection(s2)
print(s)



