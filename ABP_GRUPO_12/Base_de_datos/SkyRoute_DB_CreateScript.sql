-- CREACIÓN DE LA BBDD PARA SkyRoute S.R.L.

CREATE DATABASE IF NOT EXISTS skyroute_db; #DDL | Se crea la BBDD si no existe otra con el mismo nombre.
USE skyroute_db; #DCL permite el acceso a la BBDD

-- CREACIÓN DE LAS TABLAS.
-- DDL | Se define la extructura de la BBDD, crean las tablas y se definen los campos de las mismas con sus condiciones.

--Creación de la tabla tipo_persona
-- skyroute_db.tipo_persona definition

    CREATE TABLE IF NOT EXISTS tipo_persona (
        id_tipo_persona INT PRIMARY KEY AUTO_INCREMENT,
        descripcion VARCHAR(50) NOT NULL
    )


-- Creación de la tablas de Clientes
-- skyroute_db.cliente definition

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

-- Creación de la tabla de Destinos
-- skyroute_db.destinos definition

    CREATE TABLE IF NOT EXISTS destinos (
        id_destino INT(30) PRIMARY KEY AUTO_INCREMENT,
        pais VARCHAR(100) NOT NULL,
        estado VARCHAR(100) NOT NULL,
        ciudad VARCHAR(100) NOT NULL,        
        costo_base_destino DECIMAL(10,2) NOT NULL        
    )


--Creación de la tabla estados
-- skyroute_db.estados definition

    CREATE TABLE IF NOT EXISTS estados (
        id_estado INT(30) PRIMARY KEY AUTO_INCREMENT,
        nombre_estado VARCHAR(100) NOT NULL,
        descripcion VARCHAR(100) NOT NULL  
    )

-- Creación de la tabla de Ventas
-- skyroute_db.ventas definition

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

-- Creación de la tabla para el Botón de Arrepentimiento
-- skyroute_db.boton_arrepentimiento definition

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