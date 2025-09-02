# TypeCasting = the process of converting a varaible from one data type to another str(), int(), float(), bool()

#                str(), float(), int(), bool()

bro = ""

age = 19

gpa = 3.4
is_student = True

print(type(age))
print(type(gpa))
print(type(bro))
print(type(is_student))

gpa = int(gpa)

print(f"your gpa is now {type(gpa)} = {gpa}")

age = float(age)

print(f"your age is now {type(age)} = {age}")

gpa += 1
print(f"your gpa is now increase by {gpa}")

bro = bool(bro)

print(f"your name is now boolean let's check it {bro}")
