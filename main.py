from CRUD.buscar import buscar_cliente
from CRUD.eliminar import eliminar_cliente

def menu():
    opc=""
    while opc != "6":
        print("\n Bienvenido al centro de datos")
        print("\n Seleccione una opcion: \n1-Buscar un cliente \n2-eliminar un cliente \n3-Buscar un libro \n4-Actualizar un libro \n5-Eliminar libro \n6-Salir")
        opc=input()
        if opc == "1":
            buscar_cliente()
        elif opc == "2":
            eliminar_cliente()
        elif opc == "3":
            print("Agrega tu funcion")
        elif opc == "4":
            print("Agrega tu funcion")
        elif opc == "5":
            print("Agrega tu funcion")
        elif opc == "6":
            print("Hasta luego")
menu()