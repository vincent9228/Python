# Determining grade
# Filename: Yuyq_P02Q03

# Prompt user for score.
i = int(input("Enter your score:"))

# determine the corresponding grade and print result.
if i > 70 :
    print("A")
elif 60 < i < 69 :
    print("B")
elif 55 < i < 59 :
    print("C")
elif 50 < i < 54 :
    print("D")
elif 45 < i < 49 :
    print("E")
elif 35 < i < 44 :
    print("S")
else :
    print("U")
