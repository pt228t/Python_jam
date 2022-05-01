# Collection which is unordered and unindexed
# No duplicate values are present

utensils = {"fork", "spoon","knife","spoon"}
dishes = {"bowl","plate","cup","knife"}

print(utensils)

for x in utensils:
    print(x)

utensils.add("napkin")
print(utensils)


utensils.remove("napkin")
print(utensils)

#utensils.clear()
#print(utensils)
#Adding mmultiple elements to set
#utensils.update(dishes)
#print(utensils)

#it will also act like update
#utensils.union(dishes)
#print(utensils)

#To find difference between two sets i.e which elements are not common
print(utensils.difference(dishes))
print(dishes.difference(utensils))

#To find common between the both sets 
print(utensils.intersection(dishes))
