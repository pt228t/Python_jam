#tuple is immutable which means onces created ,we cannot add, remove or modify the data inside it
# It is collection of heterogenous - string, int, float,boolean
# It non-primitive data type - basically built in data structure

T1 = (1,"a",True,"b",3,4.5)
print(T1)

#Accessing individual elements from tuple
print(T1[5])
print(T1[-2])
print(T1[1:4])
# Since tuple is immutable, we can't modify,add or delete an item inside it. So below assignation will give error
T1[5] = "c" 
T1[1] = "d"
print(T1[1])