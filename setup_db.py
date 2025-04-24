from Utils.db import conexion
import sqlite3

def create_table():
    try:
        connection = conexion()
        
        # Verificar si la tabla ya existe
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='registros'")
        table_exists = cursor.fetchone()
        
        if not table_exists:
            connection.execute('''CREATE TABLE registros
                               (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                               nombre TEXT NOT NULL,
                               correo TEXT NOT NULL,
                               telefono TEXT NOT NULL,
                               empresa TEXT NOT NULL,
                               fecha TEXT NOT NULL) ''')
            connection.commit()
            print("Tabla 'registros' creada con éxito.")
        
        connection.close()
        return True
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
        return False

if __name__ == "__main__":
    create_table()