# Calculator Project

import os
import subprocess


def clear():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)


clear()


def main():
    while True:
        while True:
            try:
                num1 = float(input("Enter the first number: "))
            except ValueError:
                print("Please enter a decimal or integer number.")
            else:
                break

        while True:
            try:
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Please enter a decimal or integer number.")
            else:
                break

        operators = ["+", "-", "*", "/"]
        while True:
            opr = input("Please enter the operator: ")
            if opr not in operators:
                print("Enter a valid operator.")
            else:
                break

        if opr == "+":
            print(f"Your answer is {num1 + num2}.")
        elif opr == "-":
            print(f"Your answer is {num1 - num2}.")
        elif opr == "*":
            print(f"Your answer is {num1 * num2}.")
        elif opr == "/":
            if num2 == 0:
                print("Can't divide by 0")
            else:
                print(f"Your answer is {num1 / num2}")

        input("Press enter to continue. ")
        clear()
        go = input("press n to exit or enter to continue. ")

        if go == "n":
            clear()
            print('Bye and coe again! ')
            print("I am happy that you used my program 😀"
                  "\nThank you for using my program\n"
                  "created by Satyaki Debnath\n"
                  "created with following every PEP - 8 style\n"
                  "My Project - Calculator\n")
            break


if __name__ == "__main__":
    main()

'''
### Description about this code: 

Finally we have created our python calculator
and it works very good. It has a clear function for clearing
the terminal and has great platform compatibility. It enforces 
strict error handling so that the user can only enter valid numbers 
and operators without crashing the program.
'''

# You can find my code in this website link in case you want to use this code:
# Created the program using PEP - 8
