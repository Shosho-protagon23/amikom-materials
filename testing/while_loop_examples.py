# Python While Loop Examples

# Example 1: Basic counting loop
print("=== Example 1: Basic counting loop ===")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

print("Loop finished!\n")

# Example 2: User input loop
print("=== Example 2: User input loop ===")
# Uncomment the lines below to run this example interactively
# while True:
#     user_input = input("Enter something (or 'quit' to exit): ")
#
#     if user_input.lower() == 'quit':
#         print("Goodbye!")
#         break
#
#     print(f"You entered: {user_input}")

print("(User input example commented out - uncomment to run interactively)\n")

# Example 3: Sum of numbers
print("=== Example 3: Sum of numbers ===")
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"Sum of numbers 1 to 10: {total}\n")

# Example 4: Factorial calculation
print("=== Example 4: Factorial calculation ===")
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"Factorial of {n}: {factorial}\n")