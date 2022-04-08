x = 0
sum1 = 0
while True:
    num = float(input("Enter the mark:"))
    x += 1
    sum1 = sum1 + num
    average=(sum1 / x)
    print(average)

    if x == 7:
        break
if average >=70:
        print('A')
elif average<70:
        print('C')
