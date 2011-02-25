# Sorting three integers
# FileName: Yuyq_P02Q06

# Prompt user to enter three integers a b and c.
a = int(input("Enter the first integer:"))

b = int(input("Enter the second integer:"))

c = int(input("Enter the third integer:"))

# Arrange the three integer in decending order and print result.
if a > b > c :
    print(a , b ,c)
elif a > c > b :
    print(a , c , b)
elif b > c > a:
    print(b , c , a)
elif b > a > c:
    print(b , a , c)
elif c > a > b :
    print(c , a , b)
else :
    print(c , b , a)
