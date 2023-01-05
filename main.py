# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import utils

while True:

    utils.menu()
    option = int(input("Opción menu: "))

    if option != 9:
        repeat_operation = 0
        while repeat_operation != 2:
            utils.operations_options(option)
            utils.pregunta()
            repeat_operation = int(input(""))
    if option == 9:
        break
