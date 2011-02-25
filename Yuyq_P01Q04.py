# Summing the digits in a integer
# File Name: Yuyq_P01Q04

# Prompt user to enter an integer between 0 and 1000.
Integer = int(input(" Enter an integer between 0 and 1000:"))

# add up all digits in the Integer.
Sum = Integer%10 + (Integer//10)%10 + (Integer//10)//10

# Print result.
print("{0:10s} {1:3}".format("Sum of all digits in the Integer =", Sum))
