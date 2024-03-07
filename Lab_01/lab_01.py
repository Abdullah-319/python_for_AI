# String Manipulation

topic = "\nString Manipulation"

print(topic.upper())

# Declaring strings using single, double, and triple quotes
single_quoted_string = 'This is a single-quoted string.'
double_quoted_string = "This is a double-quoted string."
triple_quoted_string = '''This is a triple-quoted string.
It can span multiple lines.
Useful for docstrings and preserving formatting.'''

# Accessing individual characters
my_string = "Hello, World!"
print("First character:", my_string[0])  # Accessing first character
print("Last character:", my_string[-1])  # Accessing last character

# Slicing strings
print("Substring from index 1 to 7:", my_string[1:7])  # Slicing from index 1 to 6
print("Every second character:", my_string[::2])  # Slicing with step 2

# Concatenating strings
new_string = single_quoted_string + ' ' + double_quoted_string
print("Concatenated string:", new_string)

# Explanation of single, double, and triple quotes:
"""
Single quotes (' ') and double quotes (" ") are used interchangeably to declare string literals.
Triple quotes (''' ''') are used to declare multi-line strings or strings that contain both single and double quotes.
Triple quotes are also commonly used for docstrings, which are documentation strings in Python.
"""








# Type Casting

topic = "\n\n\n\n\nType Casting"

print(topic.upper())

# Converting integer to float
num_int = 10
num_float = float(num_int)
print("Integer to Float:", type(num_float))

# Converting float to integer
num_float = 10.5
num_int = int(num_float)
print("Float to Integer:", type(num_int))

# Converting integer to string
num_int = 10
num_str = str(num_int)
print("Integer to String:", type(num_str))

# Converting float to string
num_float = 10.5
num_str = str(num_float)
print("Float to String:", type(num_str))

# Converting string to integer
num_str = "10"
num_int = int(num_str)
print("String to Integer:", type(num_int))

# Converting string to float
num_str = "10.5"
num_float = float(num_str)
print("String to Float:", type(num_float))

# Scenarios where type casting might be necessary:
"""
1. Input/Output: When receiving input from the user via input() function, it's initially in string format. If you expect numeric values, you'll need to cast them to the appropriate numeric type.
2. Mathematical operations: Sometimes you may need to perform mathematical operations on variables of different types, and you'll need to cast them to compatible types.
3. Data conversion: When working with data from external sources like files or APIs, the data may be in string format and you need to convert it to the desired data type for processing.
4. Formatting output: When constructing strings for output, you may need to concatenate numeric values with strings, requiring type casting.
5. Comparison: When comparing variables of different types, type casting may be necessary to ensure proper comparison.
"""









# Using F-strings for formatted output

topic = "\n\n\n\n\nF-strings"

print(topic.upper())

# Variables of different data types
name = "Abdullah"
age = 21
height = 6.0

# Formatted message using F-strings
formatted_message = f"Hello, my name is {name}. I am {age} years old and my height is {height} feet."
print(formatted_message)









# Working with Lists

topic = "\n\n\n\n\nLists"

print(topic.upper())

# Creating an empty list
my_list = []

# Adding elements to the list using append()
my_list.append('apple')
my_list.append('banana')
my_list.append('cherry')

print("List after appending elements:", my_list)

# Adding elements to the list using extend()
additional_fruits = ['grape', 'orange']
my_list.extend(additional_fruits)

print("List after extending elements:", my_list)

# Accessing elements using indices
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Removing elements from the list
removed_element = my_list.pop(2)  # Remove the element at index 2
print("List after removing element:", my_list)
print("Removed element:", removed_element)

# Explanation of append() and extend() methods:
"""
- append(): Adds its argument as a single element to the end of a list. The argument can be any data type, including lists. If you append a list to another list using append(), the entire list becomes one element at the end of the original list.
- extend(): Iterates over its argument adding each element to the list, effectively appending all the elements of its argument to the original list. If you extend a list with another list using extend(), each element of the second list is appended individually to the end of the original list.
"""









# Set Operations in Python

topic = "\n\n\n\n\nSets"

print(topic.upper())

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)
print("Union of sets:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# Difference between sets
difference_set1 = set1.difference(set2)
print("Difference of set1 - set2:", difference_set1)
difference_set2 = set2.difference(set1)
print("Difference of set2 - set1:", difference_set2)









# Tuples

topic = "\n\n\n\n\nTuples"

print(topic.upper())

# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Attempting to modify a tuple will result in an error
# my_tuple[0] = 10  # This will raise a TypeError: 'tuple' object does not support item assignment

# Scenarios where tuples are preferred over lists:
"""
1. Immutability: Tuples are immutable, meaning once created, their elements cannot be changed. This makes tuples suitable for situations where you want to ensure that the data remains constant throughout the program execution, preventing accidental modifications.
2. Performance: Tuples are generally faster than lists because they are immutable. Once created, a tuple's size and elements cannot change, leading to more efficient memory usage and faster iteration.
3. Use as dictionary keys: Since tuples are immutable, they can be used as keys in dictionaries, whereas lists cannot because they are mutable. This is useful in scenarios where you need to create a dictionary with composite keys.
4. Tuple unpacking: Tuples can be unpacked directly into variables, making them useful for returning multiple values from a function or for parallel assignment of variables.
5. Sequence of heterogeneous elements: Tuples can contain elements of different data types, making them suitable for representing records or data structures where each element has a specific meaning or role.
"""

# Example of tuple unpacking
x, y, *z = my_tuple
print("Tuple unpacking:", x, y, z)









# Using Dictionaries to Store Student Information

topic = "\n\n\n\n\nDictionaries"

print(topic.upper())

# Define a dictionary to store student information
student_info = {
    'Abdullah': 85,
    'Ahmad': 90,
    'Ali': 75,
    'Huzaifa': 95,
    'Hunain': 80
}

# Print the student information
print("Student Information:")
for name, grade in student_info.items():
    print(f"Name: {name}, Grade: {grade}")

# Retrieve information about a specific student
student_name = 'Hunain'
if student_name in student_info:
    print(f"\n{student_name}'s grade is {student_info[student_name]}.")
else:
    print(f"\n{student_name} is not found in the student information dictionary.")







# Loops  

# Deterministic Loop Example
    
topic = "\n\n\n\n\nDeterminnistic Loop"
print(topic.upper())  

# Fixed no. of itrations
    
for i in range(5):
    print(i)




# Non-Deterministic Loop Example
    
topic = "\n\n\n\n\nNon-Deterministic Loop"
print(topic.upper())  

# Variable no. of itrations
    
total = 0
while total < 10:
    num = int(input("Enter a number (until the total reaches 10): "))
    total += num
    print("Total so far:", total)
