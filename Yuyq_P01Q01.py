# converting Fahrenheit into Celsius.
# Filename: Yuyq_P01Q01

# Prompt user for temperature in Fahrenheit.
f = int(input("Temperature in Fahrenheit:"))

# convert temperature in Fahrenheit to Celsuis by formula (5/9)*(Fahrenheit-32)
Celsius = (5/9) * (f-32)

# print("Celsius = " , Celsius)   
print("{0:10s}{1:5.2f}".format("equivalent Celsius =", Celsius))

