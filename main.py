# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import operations as op
import utils


def square(x, y):
    return np.sq


def exponential(x, y):
    return np.power(x, y)


while True:

    utils.menu()

    option = int(input("Opción: "))

    if option != 8:
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        if option == 1:
            #print("\nSuma")
            op.addition(num1, num2)
        if option == 2:
            op.subtraction(num1, num2)
        if option == 3:
            op.division(num1, num2)
        if option == 4:
            op.multiplication(num1, num2)
        if option == 5:
            print("Raíz")
        if option == 6:
            print("Exponente")
        if option == 7:
            print("Seno")
    if option == 8:
        break
