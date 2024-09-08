# collection = single "variable" used to store multiple values

# 	List =  [] 	ordered and changeable. Duplicates OK
# 	Set  =  {} 	unordered and immutable, but Add/Remove OK. NO Duplicates
# 	Tuple = () 	ordered and unchangeable. Duplicates OK. FASTER


#Collection
fruit = "apple"
print(fruit)


#List
fruits = ["apple", "strawberry", "mango", "orange"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
# Faster way
for fruit in fruits:
	print(fruit)

#Return number of objects in list
print(len(fruits))

# Check if value is in list
print("apple" in fruits

#Change elements in lists with new value
fruits[0] = "pineapple"
for fruit in fruits:
	print(fruit)
#Add something to end of the list
fruits.append("coconut")

#Remove value
fruits.remove("mango")

#Insert at a specific location
fruits.insert(0, "mango")

fruits.sort() # Sort alphabetically
fruits.reverse()
fruits.clear # Remove all values in list
print(fruits.index("pineapple")) # Find index of a value

print(fruits.count("pineapple")) # Find number of a certain value



#Set
fruits = {"apple", "strawberry", "mango", "orange"}
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop() # Remove first element, but it's random


#Tuple
fruits = ("apple", "strawberry", "mango", "orange")
print(fruits.index("apple"))
print(fruits.count("coconut"))
for fruit in fruits:
	print(fruit)