import sqlite3

import vista

conectar = sqlite3.connect("agenda.db")
cursor = conectar.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS datos (Id INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT, Apellido TEXT, Telefono TEXT, Correo TEXT)"""
)

cursor.close()

fMain = vista.Vista()
fMain.main()
