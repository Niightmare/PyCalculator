import numpy as np
import math


def addition():
    print("\n---Suma---")

    x = int(input("Número 1: "))
    y = int(input("Número 2: "))

    return print(f"\nLa suma de {x} + {y} = {x + y} \n")


def subtraction():
    print("\n---Resta---")

    x = int(input("Número 1: "))
    y = int(input("Número 2: "))

    print(f"\nLa resta de {x} - {y} = {x - y} \n")


def multiplication():
    print("\n---Multiplicación---")

    x = int(input("Número 1: "))
    y = int(input("Número 2: "))

    print(f"\nLa multiplicación de {x} x {y} = {x * y} \n")


def division():
    print("\n---Division---")

    x = int(input("Número 1: "))
    y = int(input("Número 2: "))

    print(f"\nLa división de {x} / {y} = {x / y} \n")


def square():
    print("\n---Raíz---")
    x = int(input("Número: "))

    print(f"\nLa raíz cuadrada de {x} es: {np.sqrt(x)} \n")


def exponential():
    print("---Potenciación---")
    x = int(input("Número a elevar: "))
    y = int(input("Potenciación: "))

    print(f"\n{x} a la {y} potencia: {pow(x, y)} \n")


def seno():
    print("---Seno---")
    x = int(input("Seno de: "))
    z = math.radians(x)

    print(f"\nEl seno de {x} es {math.sin(z)} \n")


def coseno():
    print("---Coseno---")
    x = int(input("Coseno de: "))
    z = math.radians(x)

    print(f"\nEl coseno de {x} es {math.cos(z)} \n")


def tangente():
    print("---Tangente---")
    x = int(input("Tangente de: "))
    z = math.radians(x)

    print(f"\nLa tangente de {x} es {math.tan(z)} \n")

