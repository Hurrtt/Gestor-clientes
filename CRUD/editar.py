from Utils.db import conexion

def edit_client():
    try:
        conn = conexion()
        cursor = conn.cursor()

        cliente_id = input("Ingresa el ID del cliente que desea editar: ")
        if not cliente_id.isdigit():
            return "Error, el id debe ser numero."
        cliente_id = int(cliente_id)

        datos_actualizar = {}
        print("\nIngresa los nuevos datos, deja en blanco si no deseas cambiar el dato.")
        new_name = input(f"Ingresa el nuevo nombre del cliente {cliente_id}: ")
        if new_name:
            datos_actualizar["nombre"] = new_name

        new_email = input("Ingresa el nuevo correo: ")
        if new_email:
            datos_actualizar["correo"] = new_email
        
        new_phonenumber = input("Ingresa el nuevo numero de telefono: ")
        if new_phonenumber:
            datos_actualizar["telefono"] = new_phonenumber
        
        new_emprise = input("Ingresa la nueva empresa: ")
        if new_emprise:
            datos_actualizar["empresa"] = new_emprise
        new_date = input("Ingrese la nueva fecha: ")
        datos_actualizar["fecha"] = new_date
        if not datos_actualizar:
            
            return "No se proporcionaron datos para actualizar."
        
        

        updates = []
        values = []
        for key, value in datos_actualizar.items():
            updates.append(f"{key} = ?")
            values.append(value)

        sql = f"UPDATE registros SET {', '.join(updates)} WHERE id = (?)"
        values.append(cliente_id)

        conn.execute(sql,(values,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Cliente con ID {cliente_id} actualizado exitosamente.")
            conn.close()
            return True
        else:
            print(f"No se encontró ningún cliente con el ID {cliente_id}.")
            conn.close()
            return False

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        conn.close()
        return 

        

    
