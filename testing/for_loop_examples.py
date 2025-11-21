# Python For Loop Examples

# Example 1: Basic for loop with range
print("=== Example 1: Basic for loop with range ===")
for i in range(5):
    print(f"Iteration: {i}")
print()

# Example 2: Loop through a list
print("=== Example 2: Loop through a list ===")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}")
print()

# Example 3: Loop with both index and value using enumerate
print("=== Example 3: Loop with enumerate ===")
fruits = ["apple", "banana", "orange", "grape"]
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")
print()

# Example 4: Loop through a dictionary
print("=== Example 4: Loop through a dictionary ===")
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
print()

# Example 5: Loop with a step in range
print("=== Example 5: Loop with step in range ===")
for i in range(0, 10, 2):
    print(f"Even number: {i}")
print()

# Example 6: Nested loops
print("=== Example 6: Nested loops ===")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
print()

# Example 7: List comprehension style loop
print("=== Example 7: Squares of numbers ===")
squares = []
for num in range(1, 6):
    squares.append(num ** 2)
print(f"Squares: {squares}")
print()

# Example 8: Loop through string
print("=== Example 8: Loop through string ===")
word = "Python"
for char in word:
    print(f"Character: {char}")
print()