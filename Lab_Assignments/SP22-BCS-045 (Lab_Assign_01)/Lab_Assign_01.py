# Activity 1:

# Display grade of the student

marks=float(input("Enter your exam marks (0-100): "))

if marks < 0 or marks > 100:
    print("Please enter correct marks")
elif marks<50:
    print("Your grade is F")
elif marks>=50 and marks<=60:
    print("Your grade is E")
elif marks>=61 and marks<=70:
    print("Your grade is D")
elif marks>=71 and marks<=80:
    print("Your grade is C")
elif marks>=81 and marks<=90:
    print("Your grade is B")
elif marks>=91 and marks<=100:
    print("Your grade is A")


# Activity 2:
    
# Calculate factorial of the number.

number = int(input("Enter an integer number: "))

factorial = 1

if (number < 0 or number == 1):
    print(f"Factorial of {number} is 1")
else:
    for i in range(1, number + 1): 
        factorial = factorial * i

print(f"The factorial of {number} is: {factorial} ")









# Assignment:

# Calculate Fibonacci series

num2 = int(input("Enter the no. of which you want to find the fibonacci series:  "))

num1, num2 = 0, 1 
count = 0

if num2 <= 0:
    print("Please enter a positive integer.")
elif num2 == 1:
    print(f"Fibonacci sequence upto {num2} is: ")
    print(num1)
else:
    print("Fibonacci sequence: ")
    while count < num2:
        print(num1)
        next = num1 + num2
        num1 = num2
        num2 = next
        count += 1
