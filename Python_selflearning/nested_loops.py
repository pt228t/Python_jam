#we will create a rectangle


#columns = int(input("How many columns?: "))


#for i in range(rows):
#    for j in range(column,0,-1):

#    column = column-1
#    print(symbol)



#for i in range(rows):
#    for k in range(i+1):
#        print(symbol,  end=" ")
#    print()


#This below functions creates a triangle pattern-
rows = int(input("How many rows?: "))
symbol = input("what your symbol?: ")
space = rows-1
invert_rows = rows-1
invert_column = invert_rows
for j in range(rows):
    if j == 0:
        print(space*' ',end="")
        space-=1
    if j >= 1:
        print(space*' ',end="")
        print(j*symbol,end="")
        space-=1
    print((j+1)*symbol)

#This below piece will print inverted triangle
for k in range(invert_rows):
    if k < invert_rows-1:
        print((k+1)*' ',end="")
        print((invert_column-1)*symbol,end="")
        invert_column-=1
    if k == invert_rows-1:
        print((k+1)*' ',end="")
    print((rows-1)*symbol)
    rows-=1

    


