# indexing = accessing elements of a sequence using [] (indexing operator)
# 			 [start : end : step]

credit_card_number = "1234-5678-9012-3456"

print(credit_card_number[0]) # prints first digit
print(credit_card_number[0:3]) # prints first 4 digits
print(credit_card_number[5:9]) # prints next set of digits
print(credit_card_number[5:]) # prints digits from a point to the end
print(credit_card_number[-1]) # prints last digit of string
print(credit_card_number[-3]) # prints the third to last digit
print(credit_card_number[::2]) # prints every second character of the string, step

last_four_digits = credit_card_number[-4:-]
print(f"XXXX-XXXX-XXXX-{last_four_digits}")

#Reverse characters

reverse_credit_card_number = credit_card_number[::-1] # to reverse sequence, set the Step to be -1
print(reverse_credit_card_number)