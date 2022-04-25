#when we accept user input, it is always of string datatype

name = input("What is your name?: ")
print(name)
#Casting user input to int as by default it is string
age = int(input("How old are you?: "))
height = float(input("how tall are you?: "))
age = age + 1
print("Hello Bhai, tu "+str(height)+" inch lamba hai")
print("Hello Bhai, tu "+str(age)+" saal ka hai")