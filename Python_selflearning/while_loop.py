name = ""
while len(name) == 0:
    name = input("Enter your name?: ")

print("Hello "+name)

#Alternative way
name = None
while not(name):
    name = input("Enter your name?: ")

print("Hello "+name)