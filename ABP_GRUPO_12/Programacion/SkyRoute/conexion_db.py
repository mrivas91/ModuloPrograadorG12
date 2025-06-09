""" 
CRUD Agencia de viajes: "Flight Booking Management System" (Sistema de gestión de reservas de vuelos), conectado a una base de datos MySQL/MariaDB.
Este código utiliza la biblioteca mysql.connector para interactuar con la base de datos.

Primero, asegurarse tener instalada la biblioteca mysql-connector-python ejecutando:

pip install mysql-connector-python

"""

import mysql.connector 


def crear_base_datos():
    """Crea la base de datos si no existe."""
    conexion_temp = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="1991" , 
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    cursor_temp = conexion_temp.cursor()
    #Acá hay código SQL
    cursor_temp.execute("CREATE DATABASE IF NOT EXISTS skyroute_db") # agenda_db se llamará la base de datos (puedes elegir el nombre que desees)
    conexion_temp.close()

def crear_tabla_si_no_existe(conexion):
    """Crea las tablas si no existen."""
    cursor = conexion.cursor()

    # Crear tabla tipo_persona
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tipo_persona (
        id_tipo_persona INT PRIMARY KEY AUTO_INCREMENT,
        descripcion VARCHAR(50) NOT NULL
    )
    """)
    #inserta los registros a la tabla tipo_persona
    cursor.execute("INSERT IGNORE INTO tipo_persona (id_tipo_persona, descripcion) VALUES (1, 'Persona física'), (2, 'Persona jurídica')")
    conexion.commit()

    # Crear tabla cliente
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id_cliente INT(30) PRIMARY KEY AUTO_INCREMENT,
        DNI INT(11) not null,
        CUIT_CUIL VARCHAR(30),
        nombre VARCHAR(100),
        apellido VARCHAR(100),
        razon_social VARCHAR(255),
        email VARCHAR(100),
        telefono VARCHAR(20),
        id_tipo_persona INT,
        FOREIGN KEY (id_tipo_persona) REFERENCES tipo_persona(id_tipo_persona)
    )
    """)
    conexion.commit()

    #Crear tabla destinos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS destinos (
        id_destino INT(30) PRIMARY KEY AUTO_INCREMENT,
        pais VARCHAR(100) NOT NULL,
        estado VARCHAR(100) NOT NULL,
        ciudad VARCHAR(100) NOT NULL,        
        costo_base_destino DECIMAL(10,2) NOT NULL        
    )
    """)
    conexion.commit()


    #Crear tabla estados
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estados (
        id_estado INT(30) PRIMARY KEY AUTO_INCREMENT,
        nombre_estado VARCHAR(100) NOT NULL,
        descripcion VARCHAR(100) NOT NULL  
    )
    """)

    #inserta los registros a la tabla estados
    cursor.execute("INSERT IGNORE INTO estados (nombre_estado, descripcion) VALUES ('APROBADO', 'Se confirmó la venta del pasaje'), ('PENDIENTE', 'No se confirmó la venta del pasaje'), ('CANCELADO', 'El usuario utilizó el botón de arrepentimiento')")
    conexion.commit()


    #Crear tabla ventas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id_venta INT(30) PRIMARY KEY AUTO_INCREMENT,
        id_cliente INT(30) NOT NULL,
        id_destino INT(30) NOT NULL,
        fecha_venta DATETIME NOT NULL,
        id_estado INT(30) NOT NULL,  
        FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente), 
        FOREIGN KEY (id_destino) REFERENCES destinos(id_destino), 
        FOREIGN KEY (id_estado) REFERENCES estados (id_estado)   
    )
    """)
    conexion.commit()

    #Crear tabla boton_arrepentimiento
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS boton_arrepentimiento (
        id_arrepentimiento INT(30) PRIMARY KEY AUTO_INCREMENT,
        id_venta INT(30) NOT NULL,
        id_cliente INT(30) NOT NULL,
        id_destino INT(30) NOT NULL,
        fecha_venta DATETIME NOT NULL,
        fecha_arrepentimiento DATETIME NOT NULL,
        id_estado INT(30) NOT NULL,
        FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),                    
        FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente), 
        FOREIGN KEY (id_destino) REFERENCES destinos(id_destino), 
        FOREIGN KEY (id_estado) REFERENCES estados (id_estado)   
    )
    """)
    conexion.commit()

# Crear la base de datos si no existe
crear_base_datos()

# Configuración de la conexión a la base de datos

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1991",
        database="skyroute_db",
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )

# este codigo permite probar la conexion si se ejecuta conexion_db.py

if __name__ == "__main__":
    crear_base_datos()
    conexion = conectar()
    crear_tabla_si_no_existe(conexion)
    conexion.close()
    print("Se cerro la conexion ok.")

# Las conexiones se abren y cierran desde otras funciones cuando se usan.