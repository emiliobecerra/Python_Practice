
name = input("Enter your full name: ")

result = len(name)
print(result) # Length of a string

result = name.find(" ")
print(result) # returns the position of the space

result = name.rfind("o") # returns position of last occurence
print(result)

name = name.capitalize()
print(name) # Returns capitalized first word

name = name.upper()
print(name) # Returns all upper case letters

name = name.lower()
print(name) # returns all lower case letters

result = name.isdigit()
print(result) # returns True if string ONLY contains digits

result = name.isalpha()
print(result) # returns True if strong ONLY contains alphabetical values, not including spaces.



phone_number = input("Enter your phone number: ")
# 1-234-567-8901

result = phone_number.count("-") 
print(result) # returns the number of occurences of a value

phone_number = phone_number.replace("-", "")
print(phone_number) # replaces all selected values with value of choice

print(help(str))


#Excercise:
# Validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

username.find(" ")

if len(username) > 12:
	print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
	print("Your username can't contain spaces")
elif not username.isalpha():
	print("Your username can't contain numbers")
else:
	print(f"Welcome {username}")
