#Datatype in Python - String, int, float and boolean(true/false)

# Int and string Data type examples
# Int datatype can store the number without decimal
# String datatype can only store words/characters within " " . If number is sotred within quotes, it becomes a string. 
age = 21
age = age + 42
#typecasting int to string, since python can operate on same datatype only
print("Hello,your age is "+str(age))
print(type(age))



#Float is decimal number and int datatype cannot store decimal number
height = 250.5
print(height)
print(type(height))
#typecasting float to string, since python can operate on same datatype only
print("Your height is: "+str(height)+"cm")


#Boolean is better used in IF conditon wherein string cannot be utilised
human = True
print(human)
print(type(human))