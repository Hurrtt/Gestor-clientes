from CRUD.buscar import buscar_cliente
from CRUD.eliminar import eliminar_cliente
from CRUD.agregar import agregar_cliente
from CRUD.editar import edit_client
from setup_db import create_table

def menu():
    opc=""
    while opc != "5":
        print("\n Bienvenido al centro de datos")
        print("\n Seleccione una opcion: \n1-eliminar un cliente \n2-Buscar cliente \n3-Agregar cliente \n4-Actualizar informacion de un cliente \n5-Salir")
        opc=input()
        if opc == "1":
            eliminar_cliente()
        elif opc == "2":
            buscar_cliente()
        elif opc == "3":
            agregar_cliente()
        elif opc == "4":
            edit_client()
        elif opc == "5":
            print("Hasta luego")
if __name__ == "__main__":
    create_table()  
    menu()