from Utils.db import conexion

def buscar_cliente():
    connection = conexion()
    cursor = connection.cursor()
    opc = int(input('Con que desea realizar su busqueda? \n1-Nombre \n2-Correo'))
    match opc:
        case 1:
            nombre = input("Ingrese el nombre del cliente: ")
        case 2:
            correo = input('Ingrese el correo del cliente: ')
        case _:
            print('Ingrese una opcion correcta')
    if nombre:
        query = "SELECT * FROM registros WHERE = ?"
        cursor.execute(query,(nombre,))
    else:
        query = "SELECT * FROM registros WHERE = ?"
        cursor.execute(query,(correo,))
    results = cursor.fetchall()
    for resultado in results:
        print(resultado)

buscar_cliente()

    