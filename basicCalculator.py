def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def power(x, y):
    return pow(x, y)


while True:
    print("Options: ")
    print("1: Addition")
    print("2: subtraction")
    print("3: multiplication")
    print("4: division")
    print("5: power")

    choice = input("Select an operation: (1 - 2 - 3 - 4 - 5) : ")

    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))

    if choice == "1":
        print(num1, "+", num2, "=", addition(num1, num2))
    elif choice == "2":
        print(num1, "-", num2, "=", subtraction(num1, num2))
    elif choice == "3":
        print(num1, "*", num2, "=", multiplication(num1, num2))
    elif choice == "4":
        print(num1, "/", num2, "=", division(num1, num2))
    elif choice == "5":
        print(num1, "^", num2, "=", power(num1, num2))
    else:
        print("This is not a valid operation")

    response = input("Do you want to continue?: Y / N ").upper()

    if response == "Y":
        continue
    else:
        print("Goodbye!")
        break
