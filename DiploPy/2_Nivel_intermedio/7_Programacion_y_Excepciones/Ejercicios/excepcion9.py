def action2():
    print(1 + [])  # Genera un error del tipo: TypeError


def action1():
    try:
        action2()
    except TypeError:  # Llamada mas reciente al try
        print("Try interno")


try:
    action1()
except TypeError:
    print("Try externo")
