#it is undordered collection of key-value pair enclosed within {}
#it is mutable

d1 = {"female":"Toshi","Male":"Prashant","eunuch":"Pappuji"}

print(d1.keys())

print(d1.values())

print(d1["eunuch"])

d1["eunuch"] = "Pushpaji"
print(d1["eunuch"])
print(d1.values())
print(d1)
print(d1.get("Male"))

