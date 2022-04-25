temp = int(input("what is the temperature Outside?: "))

if temp > 0 and temp < 30:
    print("Temperature is good today!")
    print("Go outside!!")
elif temp < 0 or temp > 30:
    print("Temperature is Bad today!")
    print("Don't go outside")


# Not operator

if not(temp > 0 and temp < 30):
    print("Temperature is Bad today!")
    print("Don't go outside")
elif not(temp < 0 or temp > 30):
    print("Temperature is good today!")
    print("Go outside!!")