# Dtermining leap year
# FileName: Yuyq_P02Q04

# Prompt user for a year.
year = int(input("Enter a year:"))

# determine if the year entered is a leap year and print result.
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print("leap year")
else :
    print("Non leap year")
