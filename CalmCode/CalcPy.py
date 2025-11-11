# Python calc
import math

print("==================OPERATORS===================")
print("+ (Jumlahan)\n"
"- (Kurangan)\n"
"* (kalian)\n"
"/ (Bagian)")
print("==============================================")

operator = input("Select Operator: ")
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} {operator} {num2} = {result}")
else:
    print(f"NO {operator} OPERATOR AVAILABLE!")