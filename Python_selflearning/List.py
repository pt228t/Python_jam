#it is used to store multiple items in single variable
food = ["pizza","mango","hotdog","spaghetti"]

#print(type(food))
#print(food[0])
#print(food[3])

#Chaning the food item at last
food[-1] = "musk-melon"
#print(food)

for item in food:
    print(item, end=" ")

food.append("watermelon")
print(food)

food.remove("pizza")
print(food)


food.pop()
print(food)

food.insert(0, "strawberry")
print(food)

food.sort()
print(food)

food.clear()
print(food)