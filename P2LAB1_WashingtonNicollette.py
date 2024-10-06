#Nicollette Washington
#10/02/2024
#P2LAB1
#Program that calculates the area, circumference, and diameter of a circle.

import math

#get the radius
radius = float(input("Enter the radius of the circle: "))

#Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

#Display results
print(f"Diameter:  {diameter:.1f}")
print(f"Circumference:  {circumference:.2f}")
print(f"Area:  {area:.3f}")
