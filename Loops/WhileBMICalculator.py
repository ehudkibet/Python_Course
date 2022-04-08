age=float(input("Enter your height in metres:"))
weight=float(input("Enter your weight in kg:"))
BMI= weight/(age**2)
print(BMI)

while BMI<=18:
    print("You are underweight")
    break
while BMI<=25:
    print("You have normal weight")
    break
while BMI>25:
    print("You are overweight")
    break
while BMI>30 and BMI<39:
    print("You are obese")
    break
while BMI>39:
    print("Kindly enter the correct height and weight")
    break
