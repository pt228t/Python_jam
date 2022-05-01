#tuple: collection which is ordered and immutable.
#used to group together related data

student  = ("Bro", 21, "male",21)

#find number of time an element is present
print(student.count(21))

#find the index number of an element
print(student.index(21))

for x in student:
    print(x)


if "Bro" in student:
    print("Bro is present")