#Linear Data strucutre
#Contiguous memory locations
#Access elements randomly
#Homogenus elements ie similar elements

#Applications of array
#- Storing information - Linear fashion
#- Suitable for applications that requires frequent searching

# 1-Dimensonal Array 
# -Elements are stored one after another
# -Only one subscript or index is used
# -Can be related to one row

#Array declaration:
# Datatype varname[size];
#int arr[5];
# datatype varname[] = {1,2,3,4,5};
# int arr[] = {1,2,3,4,5};
"""
arr=[]
for i in range(5):
    arr.append(0)
print(arr)
"""
    
#2D Array
# It can be a table or matrix
# Elements are stored one after another ie one 1D array inside other
# Two subscripts or indices are used, one row and one column
# Dimensions depends upon the number of subscripts used

# Use_Case 1 - Create an array of size n(taking an input from user) and then do the insertion of element(taking input from user) 
# and then access those elements
"""
arr=[]
size = int(input("Enter the size of an array: "))
for i in range(size):
    print("Enter the element number ",i+1)
    element = input()
    arr.append(element)
print("Accessing the inserted element now")
for i in range(size):
    print(arr[i],end=' ')
print()
"""


#Use _Case 2 - Create 2D integer array and insert the numbers to maximum size provided until end of array.
# Access the number inserted and display the output
"""
arr=[]
size = int(input("Enter the size of an array: "))
for i in range(size):
    for j in range(size):
        print("Enter the element number ",j+1," for", i+1," parent array")
        element = int(input())
        arr.append(element) 
        #print(arr[i][j]))
print("Accessing the inserted element now")
for i in range(size):
    for j in range(size):
        print(arr[i][j])
"""
"""
n=5
arr = [0]*5
print(arr)
"""


# Ways of creating 2D array in python usinng list
"""
rows,col = 2,3
arr = [[0]*col]*rows
for i in range(rows):
    for j in range(col):
        #print("Enter the element number ",j+1," for", i+1," parent array")
        #element = int(input())
        arr[i][j] = rows*col
print(arr)

rows,col= 2,3
twod_arr = [[0 for i in range(col)]for j in range(rows)]

for i in range(rows):
    for j in range(col):
        twod_arr[i][j]= i*j
print(twod_arr)
"""

rows=[]

for i in range(3):
    col=[]
    for j in range(3):
        print("Enter the element number at position ",j+1," for index", i+1)
        element = int(input())
        col.append(element)
    rows.append(col)
    print(rows)
