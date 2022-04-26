#It is mutable - we can add,modify,delete the data in it 
#It is collection of heterogenous - string, int, float,boolean
#It non-primitive data type - basically built in data structure
# it is ennclosed within []
#it is ordered collection

l1 = [1,"a",True,2,"b",False]
print(l1)

#Replacing the data in index 1
l1[1] = "c"
print(l1)


print(l1[2:6])

#Adding element to new index position
l1.append("Prashant")
print(l1)

#Adding list inside the list
l1.append([3,4,5,6,"Toshi"])
print(l1)

#Removing element at 0 index
l1.pop(0)
print(l1)

#Removing element from last
l1.pop()
print(l1)