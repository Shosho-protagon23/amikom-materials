# x = 3.14
# y = 4
# z = 5
# # result = round(x)
# # result = abs(y)
# # result = pow(4, 3)
# # result = max(x, y, z)
# # result = min(x, y, z)
# print(result)
# x = 9.9
# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)
# print(result)

import math

# radius = float(input('Enter radius of the circle: '))
# circumference = 2 * math.pi * radius
# print(f"the circumference is {round(circumference, 2)} cm")

# radius = float(input("Radius of the circle: "))
# area = math.pi * pow(radius, 2)
# print(f'the area of the circle is {round(area, 2)} cm^2')

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"Side C is: {c}")