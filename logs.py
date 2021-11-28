# ------------------------- Imports ------------------------- #
import datetime


# ------------------ Defino la funcion log ------------------ #
def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Se inicio la agenda " + " el " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val

    return wrapper
