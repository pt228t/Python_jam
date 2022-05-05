#indexoperator[]: gives access to a sequence's element (str,list and tuples)

name = "bro Code!"
if(name[0].islower()):
    print("It is lower,changing it to upper case")
    #capitalize just makes the first letter as capital and rest as lower 
    name = name.capitalize()
    print(name)
else:
    print("it is already upper")
    

first_name = name[0:3].upper()
#OR 
first_name = name[:3].upper()
print("Making the first 3 char in upper case: "+name)



last_name = name[4:].upper()
print("Last name is: "+last_name)

last_character = name[-1]
print("Last character is: "+last_character)