print("I am printing")

# Variables


#Strings
first_name = "Emilio"
food = "pizza"
email = "emiliob@clemson.edu"
print(first_name)

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")

#Integers
age = 23
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 10.99
gpa = 3.62
distance = 5.5 
print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} mi")

# Boolean
is_student = True
for_sale = True
is_online = False

print(f"Are you a student?: {is_student}")

if is_student:
	print("You are a student")
else: 
	print("You are not a student")

if for_sale:
	print("That item is for sale")
else:
	print("That item is not available")

if is_student:
	print("you are online")
else:
	print("You are not online")

# Typecasting

name = "Emilio Becerra"
age = 23
gpa = 3.62
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

# age = float(age)
# print(age)

age = str(age)
age += "1"
print(age)


name = bool(name)
print(name)

# Input

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))

# age = age + 1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old")

# Excercise 1 Rectangle Area Calc
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is: {area}cm²")

# Excercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?"))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} X {item}/s")
print(f"Your total is: ${total}")





























print(type(gpa))


