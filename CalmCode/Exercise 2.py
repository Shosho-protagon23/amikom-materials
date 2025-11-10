# Exercise 2 Shopping Cart Program

item = input("What do you need?: ")
price = float(input("How much cost?: "))
quantity = int(input("How much do you need?: "))

total = price * quantity

print(f"You've bought {quantity} x {item}/s")
print(f"Your total is: ${total}")