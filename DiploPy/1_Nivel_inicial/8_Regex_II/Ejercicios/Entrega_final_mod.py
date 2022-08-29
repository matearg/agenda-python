# Modulos importados
import os
import sqlite3
import time

conectar = sqlite3.connect("agenda.db")
cursor = conectar.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS datos (Id INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT, Apellido TEXT, Telefono TEXT, Correo TEXT)"""
)

cursor.close()


def agregar():

    "Agrega un nuevo contacto a la Agenda"

    print("Agregar contacto")
    print("----------------")
    print("")

    conectar = sqlite3.connect("agenda.db")
    cursor = conectar.cursor()

    Id = None
    Nombre = input("Nombre: ")
    Apellido = input("Apellido: ")
    Telefono = input("Telefono: ")
    Correo = input("Correo: ")

    cursor.execute(
        "INSERT INTO datos (Nombre, Apellido, Telefono, Correo) VALUES ('%s','%s','%s','%s')"
        % (Nombre, Apellido, Telefono, Correo)
    )

    conectar.commit()
    cursor.close()

    print("")
    input("Los datos fueron agregados correctamente ")


def ver():

    "Devuelve todos los contactos de la agenda"

    print("Lista de contactos")
    print("------------------")
    print("")

    conectar = sqlite3.connect("agenda.db")
    cursor = conectar.cursor()

    cursor.execute("SELECT * FROM datos")
    resultado = cursor.fetchall()

    for i in resultado:
        print("%s, %s, %s, %s, %s" % (i[0], i[1], i[2], i[3], i[4]))

    cursor.close()

    print("")
    input("Presione una tecla para continuar ")


def buscar():

    "Busca un contacto en la agenda y lo lista"

    print("Buscar contacto")
    print("---------------")
    print("")

    conectar = sqlite3.connect("agenda.db")
    cursor = conectar.cursor()

    buscar = input("Id de contacto a buscar: ")

    cursor.execute("SELECT * FROM datos WHERE Id = '%s'" % (buscar))

    x = cursor.fetchall()

    print("")

    for i in x:
        print("Id:", i[0])
        print("Nombre:", i[1])
        print("Apellido:", i[2])
        print("Telefono:", i[3])
        print("Correo:", i[4])

    cursor.close()

    print("")
    input("Presione una tecla para continuar ")


def eliminar():

    "Elimina un contacto de la Agenda"

    print("Eliminar contacto")
    print("---------------")
    print("")

    conectar = sqlite3.connect("agenda.db")
    cursor = conectar.cursor()

    eliminar = input("Id de contacto a eliminar: ")

    cursor.execute("DELETE FROM datos WHERE Id = '%s'" % (eliminar))

    conectar.commit()

    cursor.close()

    print("")
    input("Contacto eliminado correctamente ")


def modificar():

    "Modifica un contacto de la Agenda y lo lista"

    conectar = sqlite3.connect("agenda.db")
    cursor = conectar.cursor()

    print("")
    Id = input("Id de contacto a modificar: ")
    print("")

    Nombre = input("Nombre: ")
    Apellido = input("Apellido: ")
    Telefono = input("Telefono: ")
    Correo = input("Correo: ")

    sql = """UPDATE datos SET Nombre = ?, Apellido = ?, Telefono = ?, Correo = ? WHERE Id = ?;"""
    datos = (Nombre, Apellido, Telefono, Correo, Id)
    cursor.execute(sql, datos)

    print("")
    print("Luego de modificar: ")
    print("")

    data = cursor.execute("""SELECT * FROM datos""")
    for row in data:
        print(row)
    conectar.commit()

    cursor.close()

    print("")
    input("Contacto modificado correctamente ")


def main():
    print("Agenda")
    print("------------------")
    print(
        """
        [1] Ingresar Contacto
        [2] Listar Contactos
        [3] Buscar Contacto
        [4] Eliminar Contacto
        [5] Modificar Contacto
        [0] Salir
        """
    )

    opcion = input("Ingresa una opcion -> ")

    if opcion == "1":
        os.system("cls")
        agregar()
        os.system("cls")
        main()

    elif opcion == "2":
        os.system("cls")
        ver()
        os.system("cls")
        main()

    elif opcion == "3":
        os.system("cls")
        buscar()
        os.system("cls")
        main()

    elif opcion == "4":
        os.system("cls")
        eliminar()
        os.system("cls")
        main()

    elif opcion == "5":
        os.system("cls")
        modificar()
        os.system("cls")
        main()

    elif opcion == "0":
        print("")
        print("¿Realmente desea Salir? (Y/N): ")
        print("")
        respuesta = input()
        if respuesta.lower() == "y":
            print("")
            print("Adios!")
            print("")
            time.sleep(1)
            exit()
        elif respuesta.lower() == "n":
            print("")
            os.system("cls")
            main()
        else:
            print("")
            input("La opcion elegida es invalida ")
            os.system("cls")
            main()

    else:
        print("")
        input("Opcion incorrecta ")
        os.system("cls")
        main()


main()
