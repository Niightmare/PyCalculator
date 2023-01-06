# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import utils

while True:

    utils.menu()
    option = int(input("Opción menu: "))

    if option <= 10:
        if option != 10:
            repeat_operation = 0

            while True:
                if repeat_operation == 0:
                    utils.operations_options(option)
                utils.pregunta()
                repeat_operation = int(input(""))

                if repeat_operation > 2:
                    print("\nUps! Opción incorrecta\n")
                elif repeat_operation == 1:
                    repeat_operation = 0
                elif repeat_operation == 2:
                    break

        if option == 10:
            break
    else:
        print("\nOpción incorrecta!!\n")
