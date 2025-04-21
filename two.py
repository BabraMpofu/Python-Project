# Multiplication table generator

# Input validation using a while loop
valid_entry = False
while not valid_entry:
    num = int(input("Enter an integer value greater than 1: "))#ask the user to input
    if num > 1:
        valid_entry = True
    else:
        print("Invalid entry. Please enter a value greater than 1.")#this is for printing

# Display the multiplication table
print(f"\nMultiplication table for {num}:")
for i in range(1, 6):
    result = i * num
    print(f"{i} x {num} = {result}")

# Calculate the total
total = sum(i * num for i in range(1, 6))

# Display the total
print(f"\nTotal of the multiplication table: {total}")
