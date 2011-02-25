# Computing the volume of a cylinder
# File Name: Yuyq_P01Q02

# prompt user for length in meter.
length = float(input(" Enter length in m:"))

# Prompt user for radius.
radius = float(input(" Enter radius:"))

# Import math from library.
import math
pi = math.pi

# Formula for area= radius * radius * pi
area = radius * radius * pi
# Formula for volume = area * length
volume = area * length

# Print result.
print("{0:10s} {1:5.2f} " .format("area of the cylinder = ", area))
print("{0:10s} {1:5.2f}".format ("Volume of the cylinder =", volume))
