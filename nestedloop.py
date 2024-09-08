# nested loop = A loop within another loop (Outer, Inner)
#					outer loop:
# 							inner loop:

for x in range(3):
	for y in range(1, 10):
		print(y, end="")
	print()


#print a rectangle using a symbol
rows = int(input("Enter the number of rows: "))
columns= int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
	for y in range(columns):
		print(symbol, end="")
	print()