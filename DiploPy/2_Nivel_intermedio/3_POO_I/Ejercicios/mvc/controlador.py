from tkinter import Tk
from vista import VistaApp


class MiApp:
    def __init__(self, window):
        self.ventana = window
        VistaApp(self.ventana)


if __name__ == "__main__":
    root = Tk()
    obj = MiApp(root)
    root.mainloop()
