# logical operators = evaluate multiple conditions (or, and, not)
#                     or --> setidaknya satu kondisi harus TRUE
#                     and --> kedua kondisi harus TRUE
#                     not --> membalikkan kondisi (not FALSE, not TRUE)

# OR
# temp = 20
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("outdoor canceled")
# else:
#     print("lets go")

# AND
temp = int(input("Enter temp: "))
is_sunny = False

if temp >= 28 and is_sunny:
    print("It's hot outside")
    print("it's sunny")
elif temp <= 0 and is_sunny:
    print("It's cold dawg")
    print("It's sunny")
elif 28 > temp > 0 and is_sunny:
    print("It's warm outside")
    print("It's sunny")

# NOT
if temp >= 28 and not is_sunny:
    print("It's hot outside")
    print("it's cloudy")
elif temp <= 0 and not is_sunny:
    print("It's cold dawg")
    print("It's cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It's warm outside")
    print("It's cloudy")