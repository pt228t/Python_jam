#it is key-value pair
#it is unordered collection
#it is mutable
#Fast because they use hashing and allow us to access value quickly

Identity = {"Name":"Prashant", "Class":"12th","age":28,}

capitals = {'USA':'Washington','china':'beijing', 'UK':'London', 'India':'Delhi','Russia':'Moscows'}
#It will print the value of india
print(capitals["India"])
#It will print all the keys 
print(capitals.keys())

#it will prrint all the values
print(capitals.values())

#It will try to give Keyerror if Key is not found
#print(capitals["Germany"])

# TO be safe from Key error ,we can us get method 
print(capitals.get("Germany"))


print(capitals.items())


for key,value in capitals.items():
    print(key,value)


capitals.update({"Himachal":"shimla"})
print(capitals)

#we can override the value of key also
capitals.update({"Himachal":"kullu"})
print(capitals)


#Take the key along with the value out of the dictionary
capitals.pop("Himachal")
print(capitals)


#Clear the entire dictionary
capitals.clear()
print(capitals)