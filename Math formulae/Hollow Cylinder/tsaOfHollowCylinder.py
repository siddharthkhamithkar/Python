from math import pi
r = input("What is the inner radius of the Cylinder? ")
R = input("What is the outer radius of the Cylinder? ")
h = input("What is the height of the Cylinder? ")
values = [r, R, h]
print 2 * pi * r * h + 2 * pi * (R ^ 2 - r ^ 2)
print values
