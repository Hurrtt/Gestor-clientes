from Utils.db import conexion

def buscar_cliente():
    connection = conexion()
    cursor = connection.cursor()
    opc = int(input('Con que desea realizar su busqueda? \n1-Nombre \n2-Correo'))
    match opc:
        case 1:
            nombre = input("Ingrese el nombre del cliente: ")
            query = "SELECT * FROM registros WHERE nombre = ?"
            cursor.execute(query,(nombre,))
        case 2:
            correo = input('Ingrese el correo del cliente: ')
            query = "SELECT * FROM registros WHERE correo = ?"
            cursor.execute(query,(correo,))
        case _:
            print('Ingrese una opcion correcta')
    results = cursor.fetchall()
    for resultado in results:
        print(resultado)
    cursor.close()

    