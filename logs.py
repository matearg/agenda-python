import datetime


def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Se llamo a la funcion " + " ".join([str(arg) for arg in args]) + " el " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val

    return wrapper
