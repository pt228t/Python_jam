age = int(input("How Old are you?: "))

if age == 100:
    print("You are century old!")
elif age >=18:
    print("You are adult!")
elif age < 0:
    print("You are not born yet")
else:
    print("You are a child!")