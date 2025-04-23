from Utils.db import conexion
import sqlite3

def create_table():
    try:
        connection = conexion()
        connection.execute("CREATE TABLE registros(' \
        '                   ID INTEGER PRIMARY KEY AUTOINCREMENT,' \
        '                   nombre TEXT NOT NULL,' \
        '                   correo TEXT NOT NULL,' \
        '                   telefono TEXT NOT NULL,' \
        '                   empresa TEXT NOT NULL,' \
        '                   fecha TEXT NOT NULL) ")
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error as e:
        print(f"Error al problar la tabla: {e}")

create_table() 