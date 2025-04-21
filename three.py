#45670544 Babra Mpofu
# Prompt the user for student number and name
information = input("Enter your student number and name (comma delimited): ")

# Extract student number and name using a loop
student_number = ""
name = ""
comma_found = False

for char in information:
    if char == ",":
        comma_found = True
    elif comma_found:
        name += char
    else:
        student_number += char

# Print the student number and name
print("Student Number:", student_number)
print("Name:", name)
