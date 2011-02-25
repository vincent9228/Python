# Finding the number of days in a month
# FileName: Yuyq_P02Q05

# Prompt user for month in number.
m = int(input("Enter a month in number:"))

# Prompt user for a year.
year = int(input("Enter a year:"))

# All the moneth in order.
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
         'september', 'October', 'November', 'December']

# Determine the number of day in the month and print result.
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print(month[m-1], year,"has",31,"days")
elif m == 4 or m == 6 or m == 9 or m == 11 :
    print(month[m-1],year,"has" , 30,"days")
elif m == 2 and year % 4 == 0 :
    print(month[m-1],year,"has",29,"days")
else:
    print(month[m-1],year,"has",28,"days")

