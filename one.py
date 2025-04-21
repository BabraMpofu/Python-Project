#Babra Mpofu 45670544
# Program to compare two numbers and display the result

# Input variables
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Processing
if num1 > num2:
    print("First number is greater")
elif num1 < num2:
    print("Second number is greater")
else:
    print("Both numbers are equal")

# Loop to display numbers in a range
print("Numbers in the range:")
for i in range(num1, num2 + 1):
    print(i)
