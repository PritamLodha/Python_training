from math import *

i = int(input("1.Basic  2.Scientific: "))

if i == 1:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = int(input("1.Add 2.Sub 3.Mul 4.Div: "))

    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1 / num2)

elif i == 2:
    choice = int(input("1.Sin 2.Cos 3.Tan 4.Log: "))

    if choice in [1, 2, 3]:
        num = float(input("Enter angle in degrees: "))
        if choice == 1:
            print(sin(radians(num)))
        elif choice == 2:
            print(cos(radians(num)))
        else:
            print(tan(radians(num)))

    elif choice == 4:
        num = float(input("Enter number: "))
        base = float(input("Enter base: "))
        print(log(num, base))