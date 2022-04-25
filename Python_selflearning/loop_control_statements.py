#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your Name?: ")
    if name != "":
       break

phone_number = "+91-9501834282"
for i in phone_number:
    if i == "+" or i == "-":
        pass
    else:
        print(i, end="")
print()


for i in phone_number:
    if i == "+" or i == "-":
        continue
    print(i, end="")
print()