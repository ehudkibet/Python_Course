#First 50 terms

num1 = 1
num2 = 0
s = 1
for n in range(0, 50):
    print(s)
    s = num1 + num2
    num2 = num1
    num1 = s

