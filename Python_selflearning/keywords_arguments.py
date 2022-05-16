#Keywords_arguments - arguments preceded by an identifier when we pass them to a function.
# The order of arguments does not matter, unlike positional arguments. 
# Python knows the name of the arguments that our function recieves

def hello(first,middle,last):
    print("Hello " + first +" " + middle + " "+ last)


hello("prashant", "thakur" ,"stud")
hello("thakur", "prashant", "stud")
hello(last="stud", middle="Thakur", first="Prashant")
