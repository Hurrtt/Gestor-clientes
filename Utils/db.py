import sqlite3 
import os



def conexion():
    try:
        connection = sqlite3.connect('clientes.db')
        if os.path.exists('clientes.db'):
            return connection
        
    except sqlite3.Error as e:
        print(f'La base de datos no se pudo crear con exito{e}')

conexion()