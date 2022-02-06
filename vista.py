# ------------------------- Imports ------------------------- #
import os
import time

import modelo

# --------------------- Creo las clases --------------------- #


class Vista:

    # ---------------------- Creo el menu ----------------------- #
    def main(self):
        "" "Crea el menu que se mostrará en el prompt" ""

        c_modelo = modelo.Modelo()
        c_modelo.conexion()

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
            a_modelo = modelo.Modelo()
            a_modelo.agregar()
            os.system("cls")
            self.main()

        elif opcion == "2":
            os.system("cls")
            v_modelo = modelo.Modelo()
            v_modelo.ver()
            os.system("cls")
            self.main()

        elif opcion == "3":
            os.system("cls")
            b_modelo = modelo.Modelo()
            b_modelo.buscar()
            os.system("cls")
            self.main()

        elif opcion == "4":
            os.system("cls")
            e_modelo = modelo.Modelo()
            e_modelo.eliminar()
            os.system("cls")
            self.main()

        elif opcion == "5":
            os.system("cls")
            m_modelo = modelo.Modelo()
            m_modelo.modificar()
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
