n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))
n3=float(input("Enter the third number:"))

if (n1>n2 and n1>n3):
    print("The first number is the largest")
elif (n2>n3 and n2>n1):
    print("The second number is the largest")
elif (n3>n2 and n3>n1):
    print("The third number is the largest")
else:
    print("Enter three different numbers")






