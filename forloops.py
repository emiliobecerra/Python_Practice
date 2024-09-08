# for loops = execute a block of code a fixed number of times. 
# 				You can iterate over a range, string, sequence, etc. 

for x in range(1, 11):
	print(x)


for x in reversed(range(1, 11)):
	print(x)
print("Happy New Year")


for x in reversed(range(1, 11, 2)):
	print(x)


credit_card = "1234-5678-9012-3456"
for x in credit_card:
	print(x)

#skip over a number
for x in range(1, 21):
	if x == 13:
		continue
	else:
		print(x)



#Count Down Timer Program
import time

my_time = int(input("Enter the time in seconds: "))

for x in (range(my_time, 0, -1):
	seconds = x % 60
	minutes = int(x / 60) % 60
	hours = int(x / 3600)
	print(f"{hours:02}:{minutes:02}:{seconds:02}")
	time.sleep(1)


print("Time's Up")