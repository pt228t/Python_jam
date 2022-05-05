#function : A block of code which is executed only when it is called
import time

def hello(name):
    print("Hello "+name+"!")
    print("Have a nice day and Enjoy your party!")
    time.sleep(1)

Users = []
count = input("Enter the number of people coming to party:")

for i in range(int(count)):
    print("Enter the name of individual number "+str(i+1)+" coming to the party: ")
    user = input()
    Users.append(user)

for i in range(len(Users)):
    hello(Users[i])



def hello(first_name, last_name):
    print("Hello "+first_name+" "+last_name)

hello("Prashant","Thakur")