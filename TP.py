# Step 1: Basic output
print("Welcome to the Git exercise!")

# Step 2: A simple calculation (buggy)
def subtract(a, b):
     return a - b  # Bug: should be a - b
print("6 - 2 =", subtract(6, 2))
print("I am adding this line")

from dev_A_tools import greet
print(greet("Dev.A"))

# Step 3: Random fun
import random
print("Lucky number:", random.randint(1, 100))

from dev_B_tools import square
print("Square of 4:", square(4))

# Step 4: Final message
print("Congratulations, blabla!")

# Step 5: Multiplication
# def multiply(a, b):
#     return a * b
# print("3 * 4 =", multiply(3, 4))

# Step 6: User input
# name = input("Enter your name: ")
# print("Hello,", name)

# Step 7: List processing
# numbers = [1, 2, 3, 4, 5]
# print("Sum of list:", sum(numbers))