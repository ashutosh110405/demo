# create a calculator 
while True:
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit (exit)")

    choice = input("Enter choice (+, -, *, /, exit): ")

    if choice == 'exit':
        print("Exiting the calculator.")
        break

    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        elif choice == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")

        elif choice == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        elif choice == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error! Division by zero.")
    else:
        print("Invalid input. Please try again.")
