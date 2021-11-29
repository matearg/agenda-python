# ------------------------- Imports ------------------------- #
import sqlite3
import re
import decorador

# --------------------- Creo las clases --------------------- #


class Modelo:

    re_numeros = r"[0-9]"
    re_nombres = r"[A-Za-z]"
    re_mail = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}\b"

    # ----------------- Creo la conexion a la DB ---------------- #
    def conexion(self):
        conectar = sqlite3.connect("agenda.db")
        cursor = conectar.cursor()

        try:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS datos (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Nombre TEXT NOT 
                NULL, Apellido TEXT NOT NULL, Telefono TEXT NOT NULL, Correo TEXT NOT NULL) """
            )
        except Exception:
            raise "La tabla ya existe o no se a podido crear "

        cursor.close()

    # ---------------------- Alta de datos ---------------------- #
    @decorador.alta_decorador
    def agregar(self):
        "" "Agrega un nuevo contacto a la Agenda" ""

        print("Agregar contacto")
        print("----------------")
        print("")

        conectar = sqlite3.connect("agenda.db")
        cursor = conectar.cursor()

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Telefono: ")
        correo = input("Correo: ")

        try:
            if (
                re.match(self.re_nombres, nombre)
                and re.match(self.re_nombres, apellido)
                and re.match(self.re_mail, correo)
                and re.match(self.re_numeros, telefono)
            ):

                cursor.execute(
                    """INSERT INTO datos (Nombre, Apellido, Telefono, Correo) VALUES ('%s','%s','%s','%s')"""
                    % (nombre, apellido, telefono, correo)
                )

                conectar.commit()
                cursor.close()

                print("")
                print("Los datos fueron agregados correctamente")

            else:
                print("")
                print("Datos ingresados invalidos")

        except Exception:
            print("")
            print("No se han podido agregar los datos")

        finally:
            print("")
            input("Presione una tecla para continuar ")

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

        try:
            if re.match(self.re_numeros, buscar):

                cursor.execute(
                    "SELECT * FROM datos WHERE Id = '%s'" % buscar)

                x = cursor.fetchall()

                print("")

                for i in x:
                    print("Id:", i[0])
                    print("Nombre:", i[1])
                    print("Apellido:", i[2])
                    print("Telefono:", i[3])
                    print("Correo:", i[4])

                cursor.close()

            else:
                print("")
                print("El id ingresado no es correcto")

        except Exception:
            print("")
            print("Ha ocurrido un error en la busqueda")

        finally:
            print("")
            input("Presione una tecla para continuar ")

    # ---------------------- Baja de datos ---------------------- #
    @decorador.baja_decorador
    def eliminar(self):
        "" "Elimina un contacto de la Agenda" ""

        print("Eliminar contacto")
        print("---------------")
        print("")

        conectar = sqlite3.connect("agenda.db")
        cursor = conectar.cursor()

        eliminar = input("Id de contacto a eliminar: ")

        try:
            if re.match(self.re_numeros, eliminar):

                cursor.execute(
                    "DELETE FROM datos WHERE Id = '%s'" % eliminar)

                conectar.commit()

                cursor.close()
                print("")
                print("Datos eliminados correctamente")

            else:
                print("")
                print("El id ingresado no es correcto")

        except Exception:
            print("")
            print("Ha ocurrido un error en la eliminacion")

        finally:
            print("")
            input("Presione una tecla para continuar ")

    # ------------------ Modificacion de datos ------------------ #
    @decorador.modificar_decorador
    def modificar(self):
        "" "Modifica un contacto de la Agenda y lo lista" ""

        print("Modificar contacto")
        print("----------------")
        print("")

        conectar = sqlite3.connect("agenda.db")
        cursor = conectar.cursor()

        id = input("Id de contacto a modificar: ")
        print("")

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Telefono: ")
        correo = input("Correo: ")

        try:
            if (
                re.match(self.re_nombres, nombre)
                and re.match(self.re_nombres, apellido)
                and re.match(self.re_mail, correo)
                and re.match(self.re_numeros, telefono)
            ):
                sql = """UPDATE datos SET Nombre = ?, Apellido = ?, Telefono = ?, Correo = ? WHERE Id = ?;"""
                datos = (nombre, apellido, telefono, correo, id)
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
                print("Contacto modificado correctamente")

            else:
                print("")
                print("Datos ingresados invalidos")

        except Exception:
            print("")
            print("Ha ocurrido un error en la modificacion")

        finally:
            print("")
            input("Presione una tecla para continuar ")
