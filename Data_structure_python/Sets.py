#it is an unordered and unindexed collection of elements  enclosed within {}
#Duplcates are not allowed
#unindexed means - we can't access element or add elements using index like List
#It does not print the True boolean value specifically but prints the false boolean value

s1 = {1,"a",True}
print(s1)

s1 = {1,1,1,"a","a",True}
print(s1)

s1.add(False)
print(s1)

# add supports only one element
s1.add(True)
print(s1)
s1.add("Toshi")
print(s1)

#update will support adding multiple elements
s1.update({5,6,7})
print(s1)

s1.update([10,15,3+10j])
print(s1)