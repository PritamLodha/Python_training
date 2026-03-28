choice = int(input('''Choose what you want to do:
1. Addition
2. Subtraction
3. Multiplication
4. Division
'''))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid choice")