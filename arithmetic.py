import math

friends = 10

# friends = friends + 1 
friends += 1 # Addition
# friends =- 2 # Subtraction
friends *= 3 # Mulitplication
friends /= 2 # Division
friends **=2 # Exponenitation
remainder = friends % 3 # Modulus
print(remainder)
print(friends)

x = 3.14
y = 4
z = 5

# result = round(x)  # Rounding
# result = abs(y)    # Absolute Value
# result = pow(4, 3)   # Exponent Raising: Base, Exponent
# result = max(x, y, z)  # Finding Maximium Value
# result = min(x, y, z)  # Finding Minimum Value
# print(result)

print(math.pi)
print(math.e)

result1 = math.sqrt(math.pi) # Squareroot
result2 = math.ceil(math.e) # Raises value to nearest 
result3 = math.floor(x)
print(result1)
print(result2)
print(result3)

# # Calculate circumferenece of circle

# radius = float(input('Enter the radius of a circle: '))
# circumference = 2 * math.pi * radius
# print(f"The circumference is: {round(circumference, 2)}cm")

# # Calculate area of circle

# radius = float(input('Enter the radius of a circle: '))
# area = math.pi * pow(radius, 2)
# print(f"The area of a circle is: {round(area, 3)}cm²")

# Calculate hypotenouse of a right triangle

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")