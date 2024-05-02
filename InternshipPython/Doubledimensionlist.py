# Matrix printing
rows=int(input())
cols=int(input())
mat=[]
for i in range(rows):
    rows=[]
    for j in range(cols):
        ele=int(input())
        rows.append(ele)
    mat.append(rows) 
for a in range(len(mat)):
    print(mat[a])
    print()



# Sum of rows 


       