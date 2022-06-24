# ------------------------- Imports ------------------------- #
from os import system
import time

import modelo

# --------------------- Creo las clases --------------------- #


class Vista:

    # ---------------------- Creo el menu ----------------------- #
    def main(self):
        "" "Crea el menu que se mostrará en el prompt" ""

        c_modelo = modelo.Modelo()
        c_modelo.conexion()

        system("cls")

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
            a_modelo = modelo.Modelo()
            a_modelo.agregar()
            self.main()

        elif opcion == "2":
            v_modelo = modelo.Modelo()
            v_modelo.ver()
            self.main()

        elif opcion == "3":
            b_modelo = modelo.Modelo()
            b_modelo.buscar()
            self.main()

        elif opcion == "4":
            e_modelo = modelo.Modelo()
            e_modelo.eliminar()
            self.main()

        elif opcion == "5":
            m_modelo = modelo.Modelo()
            m_modelo.modificar()
            self.main()

        elif opcion == "0":
            print("\n¿Realmente desea Salir? (Y/N): \n")
            respuesta = input("-> ")
            if respuesta.lower() == "y":
                print("\nAdios!\n")
                time.sleep(1)
                system("cls")
                exit()
            elif respuesta.lower() == "n":
                self.main()
            else:
                input("\nLa opcion elegida es invalida ")
                self.main()

        else:
            input("\nOpcion incorrecta ")
            self.main()
