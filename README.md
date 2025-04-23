# 🤝 Proyecto colaborativo: Mini CRM de Clientes

# 🎯 Objetivo:

## Crear una app en consola que permita registrar y consultar información de clientes para un negocio ficticio. Incluir funciones como:

- Agregar nuevo cliente

- Buscar cliente por nombre o correo

- Editar información del cliente

- Eliminar cliente

- Ver listado completo

⸻

## 🧩 Tecnología:

- Python: para toda la lógica.

- SQLite: para guardar clientes (o se puede hacer versión sin DB primero).

- Git: para practicar ramas, merges y commits colaborativos.

- (Opcional): usar typer para hacer una CLI bonita, o tkinter para interfaz gráfica.

⸻

## 📋 Estructura de la base de datos (clientes.db):

- Campo	Tipo

- id	INTEGER PK

- nombre	TEXT

- correo	TEXT

- telefono	TEXT

- empresa	TEXT

- fecha_alta	TEXT



⸻

## 🛠️ División sugerida del trabajo (roles por persona):

**Persona	Encargado de…**

- A	Crear y poblar base de datos (setup_db.py)

- B	Función para agregar cliente

- C	Función para buscar cliente

- D	Función para editar cliente

- E	Función para eliminar cliente

- Todos	Testing y menú principal (main.py)



⸻

# 🧪 Extensiones opcionales (si van rápido):

- Agregar validación de correo/teléfono.

- Exportar clientes a CSV.

- Filtrar por fecha de alta.

- Agregar login simple de usuarios (modo multiusuario).

⸻

# 📁 Estructura del proyecto:

mini_crm/
├── clientes.db
├── setup_db.py
├── main.py
├── crud/
│   ├── agregar.py
│   ├── buscar.py
│   ├── editar.py
│   └── eliminar.py
├── utils/
│   └── db.py
├── README.md



⸻

# ✅ ¿Qué practicarán con este proyecto?

- Coordinación usando Git y ramas

- Modularización en Python

- Uso de SQLite real

- Resolución de conflictos en equipo

- Diseño simple de CLI

- Uso de issues o tableros (si usan GitHub)

⸻
