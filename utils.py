import operations as op
def menu():
    print("*******************************")
    print("     C A L C U L A D O R A     ")
    print("*******************************")

    print("""
        Selecciona una opción: 
        1) Suma
        2) Resta
        3) División
        4) Multiplicación
        5) Raíz
        6) Potenciación
        7) Seno
        8) Coseno
        9) Tangente
        10) Salir
         """)


def pregunta():
    print("""
    ¿Deseas volver a realizar la operación?
    
    1. Si
    2. No
    """)


def operations_options(option):
    if option == 1:
        op.addition()
    if option == 2:
        op.subtraction()
    if option == 3:
        op.division()
    if option == 4:
        op.multiplication()
    if option == 5:
        op.square()
    if option == 6:
        op.exponential()
    if option == 7:
        op.seno()
    if option == 8:
        op.coseno()
    if option == 9:
        op.tangente()

4
