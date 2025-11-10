# Shopping cart program

foods = []
prices = []
total_price = 0

while True:
    food = input("Enter food name (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("===== YOUR CART =====")

for food in foods:
    print(food, end=" ")

for price in prices:
    total_price += price

print()
print(f"Total price is: ${total_price}")