import math

# print(math.pi)
# print(math.e)
# print(round(math.pi))
# x = 4.9
# result = math.sqrt(5)
# result1 = math.ceil(x)
# print(result1)

# result3 = math.floor(x)
# print(result3)

# Circumference of the circle

radius = float(input("Enter the radius: "))
circumference = 2 * math.pi * radius

# print(f"Radius = {radius}, circumference = {round(circumference, 2)}cm")

area = math.pi * pow(radius, 2)

# print(f"The area of the cirlce is {round(area, 2)}cm^2")

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side c = {round(c, 2)}")


