# Program make a simple calculator

from Func import Add
from Func import Subtract
from Func import Multiply
from Func import Divide

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')

file_handler = logging.FileHandler('log.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug("--PROGRAM START--")

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
            m = str(num1) + " + " + str(num2) + " = " + str(Add.add(num1,num2))
            logger.debug(m)
        elif choice == '2':
            print(num1, "-", num2, "=", Subtract.subtract(num1, num2))
            m = str(num1) + " - " + str(num2) + " = " + str(Subtract.subtract(num1, num2))
            logger.debug(m)
        elif choice == '3':
            print(num1, "*", num2, "=", Multiply.multiply(num1, num2))
            m = str(num1) + " * " + str(num2) + " = " + str(Multiply.multiply(num1, num2))
            logger.debug(m)
        elif choice =='4':
            while num2 == 0:
                print("Can't divide by zero")
                num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", Divide.divide(num1,num2))
            m = str(num1) + " / " + str(num2) + " = " + str(Divide.divide(num1,num2))
            logger.debug(m)


        while True:
            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = input("Let's do next calculation? (yes/no): ")
            next_calculation = next_calculation.lower()
            if next_calculation == "no":
                while True:
                    s = input("Are you sure? (yes/no):")
                    s = s.lower()
                    if s == "yes" :
                        logger.debug("--PROGRAM END--")
                        print("--Exit Program")
                        exit(1)
                    elif s == "no" :
                        break
                    else :
                        print("Invalid Input")
            elif next_calculation == "yes" :
                break
            else:
                print("Invalid Input")
                continue

            break  # Are you sure? 에서 no가 입력되었을때만 작동
