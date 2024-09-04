"""
Created on Thursday 04/09/24

@author: Victor Mendoza
"""

# Metodo calculadora
def calculadora(operador, num1, num2):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        return num1 / num2
    else:
        return print("Opción valida")

# Variables
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

operador = input("Ingrese la operación que quiere realizar: ")

# Se imprime el resultado de la operación con los numeros
print("El resultado es:",calculadora(operador, num1, num2))