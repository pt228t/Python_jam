#scope = The region that variable is recognized
# A variable is only available from inside the region it is created
# A globally and locally scoped version of variable can be created 

name = "Hey bro , I am a global variable"   #global variable and available inside or outside function

def display_name():
    #name = "Code" #local scope (available only inside the function)
    print(name)

display_name()
print(name)


# Python follow rule LEGB-
# L - local
# E - Enclosing
# G - global
# B - Built-in