
print("hello")
print("welcome to my calculator")
print("Which operation do u want to perform?")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
print("5 for square")
print("6 for exponential operation")
print("7 for cube")
print("8 for square root")

operation = input()

if operation == "1":
    num1 = input("enter number 1: ")
    num2 = input("enter number 2: ")
    print("sum is" + str(int(num1) + (int(num2))))
elif operation == "2":
    num1 = input("enter number 1: ")
    num2 = input("enter number 2: ")
    print("difference is" + str(int(num1) - (int(num2))))
elif operation == "3":
    num1 = input("enter number 1: ")
    num2 = input("enter number 2: ")
    print("product is" + str(int(num1) * (int(num2))))
elif operation == "4":
    num1 = input("enter number 1: ")
    num2 = input("enter number 2: ")
    print("answer is" + str(int(num1) / (int(num2))))
elif operation == "5":
    num = input("enter number : ")
    print("square is" + str(int(num) * (int(num))))
elif operation == "6":
    num1 = input("enter number 1: ")
    num2 = input("enter number 2: ")
    print("answer is" + str(int(num1) ** (int(num2))))
elif operation == "7":
    num = input("enter number : ")
    print("cube is" + str(int(num) * (int(num)) * (int(num))))
elif operation == "8":
    num = input("enter number : ")
    print("square is" + str(int(num) * 0.5))
else:
    print("invalid input, pls enter correct input")
