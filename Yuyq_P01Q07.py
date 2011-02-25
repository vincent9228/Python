# Payroll
# File Name: Yuyq_P01Q07

# Prompt user for name.
name = str(input("Enter your Name:"))

# Prompt user for number of hours worked weekly
hour = int(input("Enter number of hours worked weekly:"))

# Prompt user for hourly rate.
rate = float(input("Enter hourly pay rate:"))

# Prompt user for CPF contribution rate in %
CPF = float(input("Enter CPF contribution rate(%)"))

# Calaulate gross pay
GP = hour * rate

# Calculate CPF contribution rate
contribution = rate * GP / 100

# Calculate Netpay
Netpay = GP - contribution

# print result.
print( "Payroll statement for =", name,)
print("{0:32s} {1:2}".format("Number of hours worked in week =", hour,))
print("{0:17s} {1:4.1f}".format("Hourly pay rate =", rate,))
print("{0:10s} {1:4.2f}".format("Gross Pay = ", GP))
print("{0:10s} {1:4.2f} {2:5s} {3:4.2f}".format("CPF Contribution at",CPF, "% = $", contribution))
print("{0:5s} {1:4.2f}".format("Net pay = ", Netpay))



