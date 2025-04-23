import sqlite3 
import os
from setup_db import create_table


def conexion():
    try:
        connection = sqlite3.connect('clientes.db')
        if os.path.exists('clientes.db'):
            print("Base de datos creada")
            if create_table(): print("Data base poblada")
            return connection
        
    except sqlite3.Error as e:
        print(f'La base de datos no se pudo crear con exito{e}')

conexion()