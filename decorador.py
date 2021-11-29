# ------------------------- Imports ------------------------- #
import datetime


# ------------------ Defino la funcion log ------------------ #
def log_decorador(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Se inicio la agenda " + "el " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val

    return wrapper

def alta_decorador(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Se agrego un contacto " + "el " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val

    return wrapper

def baja_decorador(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Se elimino un contacto " + "el " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val

    return wrapper


def modificar_decorador(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Se modifico un contacto " + "el " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val

    return wrapper