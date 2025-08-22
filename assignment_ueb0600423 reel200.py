# Integer variable
my_integer = 10

# Float variable
my_float = 3.14

# String variable
my_string = "Hello, Python!"

# Boolean variable
my_boolean = True

# Print each variable with its type
print(f"Variable: {my_integer}, Type: {type(my_integer)}")
print(f"Variable: {my_float}, Type: {type(my_float)}")
print(f"Variable: {my_string}, Type: {type(my_string)}")
print(f"Variable: {my_boolean}, Type: {type(my_boolean)}")
# Convert float to integer
float_to_int = int(19.99)
print(f"Original float: 19.99, Converted to integer: {float_to_int}, Type: {type(float_to_int)}")

# Convert integer to string
int_to_string = str(50)
print(f"Original integer: 50, Converted to string: {int_to_string}, Type: {type(int_to_string)}")

# Convert string to float
string_to_float = float("50")
print(f"Original string: '50', Converted to float: {string_to_float}, Type: {type(string_to_float)}")
# Get first name from user
first_name = input("Enter your first name: ")

# Get last name from user
last_name = input("Enter your last name: ")

# Print greeting message
print(f"Hello, {first_name} {last_name}!")
# Fixed code
age = 20
print("You are " + str(age) + " years old.")

# Explanation of the error:
# The original code `print("You are " + age + " years old.")` produces a TypeError.
# This is because you cannot directly concatenate (join) a string with an integer using the '+' operator in Python.
# To fix this, the integer variable 'age' must first be converted to a string using `str(age)` before concatenation.
# Ask for a favorite word
favorite_word = input("Enter your favorite word: ")

# Ask how many times to repeat it
repeat_times = int(input("How many times do you want to repeat it? "))

# Print the word repeated, separated by spaces
print((favorite_word + " ") * repeat_times)