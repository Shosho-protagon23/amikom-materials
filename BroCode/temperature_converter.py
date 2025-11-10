### Temperature Convertor

unit = input("Celsius or Fahrenheit? (C or F): ")
temp = float(input("Enter temperature: "))

if unit == "C":
    temp = round((9 * temp / 5) + 32, 1)
    print(f"The temperature is: {temp} Fahrenheit")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature is: {temp} Celsius")
else:
    print(f"##{unit}## is not a valid unit of measurement!!!")