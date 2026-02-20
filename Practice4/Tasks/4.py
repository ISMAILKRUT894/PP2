#1
import math
i = int(input())
print(math.radians(i))

# 2


a = float(input("Enter the first base (a): "))
b = float(input("Enter the second base (b): "))
h = float(input("Enter the height (h): "))


area = 0.5 * (a + b) * h


print("The area of the trapezoid is:", area)
#3

n = int(input("Enter the number of sides: "))
s = float(input("Enter the length of a side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print("The area of the regular polygon is:", area)

#4
base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

area = base * height

print("The area of the parallelogram is:", area)
