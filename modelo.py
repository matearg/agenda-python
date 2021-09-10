# ------------------------- Imports ------------------------- #
import sqlite3
import re

# --------------------- Creo las clases --------------------- #
class Modelo:

    # ----------------- Creo la conexion a la DB ---------------- #
    def conexion(self):
        conectar = sqlite3.connect("agenda.db")
        cursor = conectar.cursor()

        try:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS datos (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Nombre TEXT NOT NULL, Apellido TEXT NOT NULL, Telefono TEXT NOT NULL, Correo TEXT NOT NULL)"""
            )
        except:
            raise Exception("La tabla ya existe o no se a podido crear ")

        cursor.close()

    # ---------------------- Alta de datos ---------------------- #
    def agregar(self):

        "" "Agrega un nuevo contacto a la Agenda" ""

        print("Agregar contacto")
        print("----------------")
        print("")

        conectar = sqlite3.connect("agenda.db")
        cursor = conectar.cursor()

        id = None
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Telefono: ")
        correo = input("Correo: ")

        re_numeros = r"[0-9]"
        re_nombres = r"[A-Za-z]"
        re_mail = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}\b"

        try:
            cursor.execute(
                "INSERT INTO datos (Nombre, Apellido, Telefono, Correo) VALUES ('%s','%s','%s','%s')"
                % (nombre, apellido, telefono, correo)
            )

            conectar.commit()
            cursor.close()

            print("")
            input("Los datos fueron agregados correctamente ")
        except:
            print("")
            input("No se han podido agregar los datos ")

    # -------------------- Consulta de datos -------------------- #
    def ver(self):

        "" "Devuelve todos los contactos de la agenda" ""

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

    # -------------- Consulta de datos especificos -------------- #
    def buscar(self):

        "" "Busca un contacto en la agenda y lo lista" ""

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

    # ---------------------- Baja de datos ---------------------- #
    def eliminar(self):

        "" "Elimina un contacto de la Agenda" ""

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

    # ------------------ Modificacion de datos ------------------ #
    def modificar(self):

        "" "Modifica un contacto de la Agenda y lo lista" ""

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
