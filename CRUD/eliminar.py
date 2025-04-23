import sqlite3
from Utils.db import conexion


def eliminar_cliente():
    try:
        connection = conexion()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM registros")
        all_registros = cursor.fetchall()
        for registros in all_registros:
            print (registros)
        delete = int (input("Ingrese el ID del registro a borrar: "))
        query = "DELETE FROM registros WHERE ID = ?"
        connection.execute(query, (delete, ))
        connection.commit()

    except sqlite3.Error as e:
        print (f"Error : {e}")
    finally:
        connection.close()