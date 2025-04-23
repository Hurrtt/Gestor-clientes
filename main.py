from CRUD.buscar import buscar_cliente
from CRUD.eliminar import eliminar_cliente
from CRUD.agregar import agregar_cliente
from CRUD.editar import edit_client

def menu():
    opc=""
    while opc != "5":
        print("\n Bienvenido al centro de datos")
        print("\n Seleccione una opcion: \n1-Buscar un cliente \n2-eliminar un cliente \n3-Agregar cliente \n4-Actualizar informacion de un cliente \n5-Salir")
        opc=input()
        if opc == "1":
            buscar_cliente()
        elif opc == "2":
            eliminar_cliente()
        elif opc == "3":
            agregar_cliente()
        elif opc == "4":
            edit_client()
        elif opc == "5":
            print("Hasta luego")
menu()