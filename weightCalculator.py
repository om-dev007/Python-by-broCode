# Pyhton Weight Calculator

weight = float(input("Weight: "))
unit = input("Kilograms or pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
elif unit == "L":
    weight = weight / 2.205
else:
    print(f"Your weight is {weight}")