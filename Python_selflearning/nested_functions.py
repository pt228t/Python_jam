#nested function calls: function call inside other function calls
# innermost functions calls are recieved first
# returned value is used as an argument for next outer function

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)


# Alternate way doing nested function call
print(round(abs(float(input("Enter a whole positive number: ")))))


