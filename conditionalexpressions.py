# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#							Print or assign one of two values based on a condition
#							return X if condition else Y

num = 5
print("Positive" if num > 0 else "Negative")



num = 6
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)



a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)



age = 23
status = "Adult" if age >= 18 else "Child"
print(status)



temperature = 98
weather = "HOT" if temperature > 70 else "COLD"
print(weather)



user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)



