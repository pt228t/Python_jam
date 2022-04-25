# Multiple_Assignement = allows us to assign multiple variablesat the same time in one line of code.

#name = "Prashant"
#age = 21
#attractive = True
name , age , attractive = "Prashant" , 28 , True
print(name)
print(age)
print(attractive)

#if all variables have same values then multiple assignment works in different way. Example below-
Prashant = 28
Toshi = 28 
Sandhya = 28
Prashant = Toshi = Sandhya = 28
print(str(Toshi)+str(Sandhya)+str(Prashant))
print(Prashant)
print(Toshi)
print(Sandhya)
print(Toshi+Sandhya+Prashant)