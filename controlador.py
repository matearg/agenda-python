# Alumno: Mateo Arcidiacono #
# Curso: 999185859 #
# Profesor: MBA ING. Juan Barreto #
# Año: 2021 #

"" "Lanza la aplicacion" ""

# ------------------------- Imports ------------------------- #
import vista

# --------------------- Creo las clases --------------------- #


class Controlador:
    def __init__(self):
        f_main = vista.Vista()
        f_main.main()


if __name__ == "__main__":
    Controlador()
