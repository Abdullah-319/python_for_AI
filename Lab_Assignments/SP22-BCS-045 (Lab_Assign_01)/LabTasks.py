
# Question 1: Check whether a number is even or not.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("It is even")
else:
    print("It is odd")

# Question 2: Check whether a number is even or not using f-string.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} It is even")
else:
    print(f"{num} is odd")
#Alternate way
print(f"{num} is even" if num % 2 == 0 else f"{num} is odd")

# Question 3: Calculate the sum of the first 10 numbers using a while loop.
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(total)

# Question 4: Calculate the sum of the first 10 numbers using a for loop.
total = 0
for num in range(1, 11):
    total += num
print(total)

# Question 5: Accept 5 inputs from the user and display their sum using a while loop.
total = 0
count = 0
while count < 5:
    num = int(input("Enter a number: "))
    total += num
    count += 1
print(total)

# Question 6: Accept integer values from the user until 0 is entered and display the sum.
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print(total)

# Question 7: Take an input from the user and check if it is prime or not.
num = int(input("Enter a number: "))
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not prime")
        break
else:
    print(f"{num} is prime")


# STRING FUNCTIONS:
# Question 1: Capitalize a string
# Input: "hello world"
# Output: "Hello world"

s = "hello world"
print(s.capitalize())

# Question 2: Convert a string to uppercase
# Input: "hello world"
# Output: "HELLO WORLD"

s = "hello world"
print(s.upper())

# Question 3: Right-justify a string, padding with spaces
# Input: "hello"
# Output: "              hello"

s = "hello"
print(s.rjust(20))

# Question 4: Center a string, padding with spaces
# Input: "hello"
# Output: "       hello       "

s = "hello"
print(s.center(20))

# Question 5: Replace all instances of one substring with another
# Input: "hello world", "world", "python"
# Output: "hello python"

s = "hello world"
old_substring = "world"
new_substring = "python"
print(s.replace(old_substring, new_substring))

# Question 6: Strip leading and trailing whitespace
# Input: "   hello world   "
# Output: "hello world"

s = "   hello world   "
print(s.strip())
# LabTasks.txt
# Displaying LabTasks.txt.