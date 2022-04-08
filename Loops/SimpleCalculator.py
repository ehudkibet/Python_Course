while True:
    print("options")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")

    user_input = input(":").lower()
    if user_input == "quit":
        print("The program has ended")
        break
    elif user_input == "add":
        a = float(input("Enter the first number:"))
        b = float(input("Enter the second number:"))
        print("Your answer is", a + b)
    elif user_input == "subtract":
        a = float(input("Enter the first number:"))
        b = float(input("Enter the second number:"))
        print("Your answer is", a - b)
    elif user_input == "multiply":
        a = float(input("Enter the first number:"))
        b = float(input("Enter the second number:"))
        print("Your answer is", a * b)
    elif user_input == "divide":
        a = float(input("Enter the first number:"))
        b = float(input("Enter the second number:"))
        print("Your answer is", a / b)
    else:
        print("Enter the correct values")
while False:
    print("Looping.....")
