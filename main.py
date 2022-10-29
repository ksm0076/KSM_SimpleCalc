# Program make a simple calculator

from Func import Add
from Func import Subtract
from Func import Multiply
from Func import Divide


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", Add.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Subtract.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Multiply.multiply(num1, num2))
            
        elif choice =='4':
            while num2 == 0:
                print("Can't divide by zero")
                num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", Divide.divide(num1,num2))
            

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
