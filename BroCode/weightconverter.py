# Python weight converter

weight = float(input("Masukkan berat badan mu: "))
unit = input("Berat mu dalam kilograms atau Pounds? (Kg or Lb): ")

# Kilogram ke Pound
if unit == "Kg":
    weight = weight / 0.454
    unit = "Lbs."

# Pound ke Kilogram
elif unit == "Lb":
    weight = weight * 0.454
    unit = "Kgs."
else:
    print(f"##{unit}## INVALID UNIT!")

print(f"Berat badan mu adalah: {weight} {unit}")