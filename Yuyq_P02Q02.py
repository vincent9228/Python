# Validating triangles and computing perimeter
# FileName: Yuyq_P02Q02

# Prompt user for 3 sides of a triangle.
a = int(input("Enter the side:"))
b = int(input("Enter the side:"))
c = int(input("Enter the side:"))

# check if the triangle validate and print result.
if a + b > c and a + c > b and b + c > a :
    print(" valid")
else:
    print("invalid")
