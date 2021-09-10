# ------------------------- Imports ------------------------- #
import os
import time

import modelo

# --------------------- Creo las clases --------------------- #
class Vista:

# ---------------------- Creo el menu ----------------------- #
    def main(self):

        "" "Crea el menu que se mostrará en el prompt" ""

        cModelo = modelo.Modelo()
        cModelo.conexion()

        print("Agenda [^][^]")
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
            aModelo = modelo.Modelo()
            aModelo.agregar()
            os.system("cls")
            self.main()

        elif opcion == "2":
            os.system("cls")
            vModelo = modelo.Modelo()
            vModelo.ver()
            os.system("cls")
            self.main()

        elif opcion == "3":
            os.system("cls")
            bModelo = modelo.Modelo()
            bModelo.buscar()
            os.system("cls")
            self.main()

        elif opcion == "4":
            os.system("cls")
            eModelo = modelo.Modelo()
            eModelo.eliminar()
            os.system("cls")
            self.main()

        elif opcion == "5":
            os.system("cls")
            mModelo = modelo.Modelo()
            mModelo.modificar()
            os.system("cls")
            self.main()

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
                self.main()
            else:
                print("")
                input("La opcion elegida es invalida ")
                os.system("cls")
                self.main()

        else:
            print("")
            input("Opcion incorrecta ")
            os.system("cls")
            self.main()
