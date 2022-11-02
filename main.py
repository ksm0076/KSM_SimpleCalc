# Program make a simple calculator

from Func import Add
from Func import Subtract
from Func import Multiply
from Func import Divide

import logging


# 로그 인스턴스
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 로그 형식
formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')

# 로그 기록 handler
file_handler_info = logging.FileHandler('log.log')
file_handler_warn = logging.FileHandler('warning.log')

# level 설정
file_handler_info.setLevel(logging.INFO)
file_handler_warn.setLevel(logging.WARNING)

# format 설정
file_handler_info.setFormatter(formatter)
file_handler_warn.setFormatter(formatter)

# logger에 handler 추가
logger.addHandler(file_handler_info)
logger.addHandler(file_handler_warn)




logger.info("--PROGRAM START--")


while True:
    print("--Select operation--")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", Add.add(num1, num2))
            m = str(num1) + " + " + str(num2) + " = " + str(Add.add(num1,num2))
            logger.info(m)
        elif choice == '2':
            print(num1, "-", num2, "=", Subtract.subtract(num1, num2))
            m = str(num1) + " - " + str(num2) + " = " + str(Subtract.subtract(num1, num2))
            logger.info(m)
        elif choice == '3':
            print(num1, "*", num2, "=", Multiply.multiply(num1, num2))
            m = str(num1) + " * " + str(num2) + " = " + str(Multiply.multiply(num1, num2))
            logger.info(m)
        elif choice =='4':
            while num2 == 0 :   # 0으로 나누려고 할 때
                logger.warning("Try divide by zero")
                print("Can't divide by zero")
                num2 = float(input("Enter second number: "))    # num2 가 0 아니면 탈출
            print(num1, "/", num2, "=", Divide.divide(num1,num2))
            m = str(num1) + " / " + str(num2) + " = " + str(Divide.divide(num1,num2))
            logger.info(m)
    else:   # 1, 2, 3, 4 이외의 입력
        m = "Invalid Input in operation choice / Input : " + choice
        logger.warning(m)
        print("Invalid Input")
        continue
    


    while True:
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        next_calculation2 = next_calculation.lower()    # 대소문자 구분없게 만들기
        
        if next_calculation2 == "no":
            while True:
                s = input("Are you sure? (yes/no):")
                s2 = s.lower()  # 대소문자 구분없게 만들기
                if s2 == "yes" :
                    logger.info("--PROGRAM END--")
                    print("--Exit Program")
                    exit(1)
                elif s2 == "no" :
                    break
                else :  # yes/no 이외의 입력이 들어왔을 때
                    m = "Invalid Input in exit check again / Input : " + s
                    logger.warning(m)
                    print("Invalid Input")
        elif next_calculation2 == "yes" : # while문 탈출, Select operation으로 이동
            break
        else:   # yes/no 이외의 입력이 들어왔을 때
            m = "Invalid Input in next calculation check / Input : " + next_calculation
            logger.warning(m)
            print("Invalid Input")
            continue    # Let's do next calculation? (yes/no): 로 이동 (while문 탈출 못함)

        break  # Are you sure? 에서 no가 입력되었을때만 작동
