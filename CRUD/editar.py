from Utils.db import conexion

def edit_client():
    try:
        cliente_id = input("Ingresa el ID del cliente que desea editar: ")
        if not cliente_id.str.isdigit():
            return "Error, el id debe ser numero."
        cliente_id = int(cliente_id)

        datos_actualizar = {}
        print("\nIngresa los nuevos datos, deja en blanco si no deseas cambiar el dato.")
        new_name = input(f"Ingresa el nuevo nombre del cliente {cliente_id}: ")
        if new_name:
            datos_actualizar["nombre"] = new_name

        new_email = input("Ingresa el nuevo correo: ")
        if new_email:
            datos_actualizar["email"] = new_email
        
        new_phonenumber = input("Ingresa el nuevo numero de telefono: ")
        if new_phonenumber:
            datos_actualizar["numero"] = new_phonenumber
        
        new_emprise = input("Ingresa la nueva empresa: ")
        if new_emprise:
            datos_actualizar["empresa"] = new_emprise
        
        if not datos_actualizar:
            
            return "No se proporcionaron datos para actualizar."
        
        conn = conexion()
        cursor = conn.cursor()

        updates = []
        values = []
        for key, value in datos_actualizar.items():
            updates.append(f"{key} = ?")
            values.append(value)

        sql = f"UPDATE clientes SET {', '.join(updates)} WHERE id = ?"
        values.append(cliente_id)

        cursor.execute(sql, tuple(values))
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

        

    
