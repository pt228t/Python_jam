name = "Prashant Thakur"
#len(str) - it is a String method which prints the length of the word/count of chararctes in words
print(len(name))

#find(str) - it finds the index number of a character/position of character .It counts the first character as 0
print(name.find("a"))

#capitalize() - it converts the first character of string to Upper case/Capital. If there are any spaces in string then it will capitalize only the first letter of the string.
print(name.capitalize())

# upper() - it converts whole smallcase string to upper case
print(name.upper())

# lower() - it converts whole uppercase string to lower case
print(name.lower())

# isdigit() - it returns true/false depending on if our string is digit. if you have numbers in string then also it will return true as a digit. example - name = "123"
print(name.isdigit())

#isalpha()  - it returns whether the string is alphabetical or not. If there is a space in between words then this will return false. There should be no space in between
print(name.isalpha())

#count() - it counts the number of times a character is present in a string
print(name.count("a"))

#replace() - it replaces the character in a string to the desired one
print(name.replace("a", "o"))

# It is not a method instead a feature to repeat the string multiple number of times.Please refer to the example below -
print(name*3)