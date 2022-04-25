#Bunch of useful functions related to numbers. Important functions present in math module

import math

pi = 3.5
#round - round figure the number. Like 3.4 si rounded off to 3
print(round(pi))
#ceil - it rounds off the decimal number up to it's next whole integer number . Example 3.4 to 4 and 3.1 to 4
print(math.ceil(pi))

#floor - it rounds off the decimal number down to it's next whole integer number . Example 3.7 to 3 and 4.3 to 4
print(math.floor(pi))

pi = -3.5
#abs - it tells how far is number from zero
print(abs(pi))

pi = 2
#pow - it makes base number to a power
print(math.pow(pi,2)) # pi is base number and 2 is exponent

pi = 9
print(math.sqrt(pi)) #it gives the result in float type

x = -1
y = -2
z = -3
print(max(x,y,z))
print(min(x,y,z))