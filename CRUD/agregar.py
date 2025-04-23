from Utils.db import conexion
from datetime import datetime
import sqlite3

def agregar_cliente():
    try:
        conection = conexion()
        if not conection:
            print("No se pudo conectar a la base de datos")
            return
        nombre = input("Introduce el nombre del cliente: ")
        correo = input("Introduce el correo del cliente: ")
        telefono = input("Inserta el numero de telefono del cliente: ")
        empresa = input("Introduce el nombre de la empresa a la que pertenece al cliente: ")
        fechaActual = datetime.now()
        fechaConFormato = fechaActual.strftime("%d/%m/%Y")

        query = ('''INSERT INTO registros (nombre, correo, telefono, empresa, fecha) VALUES (?, ?, ?, ?)''')
        conection.execute(query, (nombre, correo, telefono, empresa, fechaConFormato))
        conection.commit()
        conection.close()
    except sqlite3.Error as error:
        print(f"Error al agregar al cliente: {error}")
    finally:
        conection.close()