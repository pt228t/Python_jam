#2D list - A list of lists

from operator import index, indexOf


drinks = ["coffee","soda", "tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","icecream"]

food = [drinks,dinner,dessert]
#print(food)
#print(food[2][1])

for item in food:
    print(item[0], end=' ')
print()

food = drinks + dinner + dessert
#print(food)
