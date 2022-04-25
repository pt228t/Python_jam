# slicing - create a substring by extracting elements from another string
# indexing[] or slice[]
# [start:stop:step]

name = "Prashant Thakur"
first_char = name[1]
first_name = name[0:5] # or name[:5]
last_name = name[0:15] # or name[0:]
funcky_name = name[1:15:3]
reverse_string = name[10::-2]

print(first_char)
print(first_name)
print(last_name)
print(funcky_name)
print(reverse_string)

#short hand 
#first_name = name[:3] means name[0:3]
#last_name = name[4:] means name[4:end]
#funky_name = name[::2] means name[0:end:2]
#reversed_name = name[::-1] means name[0:end:-1]

#Slice example below - we can use combination of positove and negative slice to get results 
website1 = "https://google.com"
website2 = "https://wikepedia.com"
slice = slice(8,-4)
#Slice is a function whereas indexing where example is given above 
print(website1[slice])
print(website2[slice])
