# Importing the respective modules
import os
import time
import datetime

# Create an app that lets the user input two numbers and let him choose the operation to perform on them using a menu.
# The input would be taken in the console and the result would be shown in the console.

# Creating a and b who are the numbers that the user will input
a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))

# Defining a function that will show the numbers
def numbers():
    print("Tus numeros son: " + str(a) + " y " + str(b), "\n")

# Defining the operations
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

# Create a function that clears the powershell terminal.
def clear():
    os.system('cls')

# Creating a menu
def menu():
    clear()
    print("Bienvenido a la calculadora!\n")
    numbers()
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    option = int(input("\nElige una opcion: "))
    if option == 1:
        print(add(a, b))
        input("\nPresiona enter para continuar ")
        menu()
    elif option == 2:
        print(subtract(a, b))
        input("\nPresiona enter para continuar ")
        menu()
    elif option == 3:
        print(multiply(a, b))
        input("\nPresiona enter para continuar ")
        menu()
    elif option == 4:
        print(divide(a, b))
        input("\nPresiona enter para continuar ")
        menu()
    elif option == 5:
        time.sleep(1)
        clear()
        exit()
    else:
        print("Opcion invalida")
        input("\nPresiona enter para continuar ")
        menu()

# Calling the menu function
if __name__ == "__main__":
    menu()
