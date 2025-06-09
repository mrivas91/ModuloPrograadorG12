-- INSERCIÓN DE DATOS EN LAS TABLAS DE SkyRoute S.R.L.
-- DML | INSERT INTO ingresa nuevos registros en las tablas, se ingresan los nombres de los campos y 
-- luego los valores para cada campo.

--Insertar datos de tipo de persona

INSERT INTO skyroute_db.tipo_persona
(id_tipo_persona, descripcion)
VALUES(1, 'Persona física');
INSERT INTO skyroute_db.tipo_persona
(id_tipo_persona, descripcion)
VALUES(2, 'Persona jurídica');

-- Insertar los datos de prueba en la tabla Cliente
INSERT INTO skyroute_db.cliente
(id_cliente, DNI, CUIT_CUIL, nombre, apellido, razon_social, email, telefono, id_tipo_persona)
VALUES(1, 34677549, '27-34677549-7', 'Mariela', 'Rivas', '-', 'myantequera@gmail.com', '26040000293', 1);
INSERT INTO skyroute_db.cliente
(id_cliente, DNI, CUIT_CUIL, nombre, apellido, razon_social, email, telefono, id_tipo_persona)
VALUES(3, 33276228, '20-33276228-2', 'Juan Ignacio', 'Alonso', '-', 'zalbak87@gmail.com', '2604000293', 1);

-- Insertar datos de prueba en la tabla Destino
INSERT INTO skyroute_db.destinos
(id_destino, pais, estado, ciudad, costo_base_destino)
VALUES(1, 'Argentina', 'Cordoba', 'Capital', 35000.00);
INSERT INTO skyroute_db.destinos
(id_destino, pais, estado, ciudad, costo_base_destino)
VALUES(2, 'Argentina', 'Mendoza', 'San Rafael', 45000.00);
INSERT INTO skyroute_db.destinos
(id_destino, pais, estado, ciudad, costo_base_destino)
VALUES(4, 'Argentina', 'Buenos Aires ', 'La Plata', 30000.00);
INSERT INTO skyroute_db.destinos
(id_destino, pais, estado, ciudad, costo_base_destino)
VALUES(6, 'Argentina', 'Neuquen', 'Neuquen', 35000.00);
INSERT INTO skyroute_db.destinos
(id_destino, pais, estado, ciudad, costo_base_destino)
VALUES(7, 'Mexico', 'Queretaro', 'Queretaro', 500000.00);

--Insertar datos de prueba en la tabla estados

INSERT INTO skyroute_db.estados
(id_estado, nombre_estado, descripcion)
VALUES(1, 'APROBADO', 'Se confirmó la venta del pasaje');
INSERT INTO skyroute_db.estados
(id_estado, nombre_estado, descripcion)
VALUES(2, 'PENDIENTE', 'No se confirmó la venta del pasaje');

-- Insertar datos de prueba en la tabla Venta
INSERT INTO skyroute_db.ventas
(id_venta, id_cliente, id_destino, fecha_venta, id_estado)
VALUES(1, 1, 4, '2025-06-08 13:38:58.000', 1);
INSERT INTO skyroute_db.ventas
(id_venta, id_cliente, id_destino, fecha_venta, id_estado)
VALUES(2, 1, 1, '2025-06-08 17:09:54.000', 3);
INSERT INTO skyroute_db.ventas
(id_venta, id_cliente, id_destino, fecha_venta, id_estado)
VALUES(3, 1, 4, '2025-06-08 17:13:41.000', 3);
INSERT INTO skyroute_db.ventas
(id_venta, id_cliente, id_destino, fecha_venta, id_estado)
VALUES(4, 1, 1, '2025-06-08 17:30:01.000', 2);
INSERT INTO skyroute_db.ventas
(id_venta, id_cliente, id_destino, fecha_venta, id_estado)
VALUES(5, 1, 1, '2025-06-08 17:37:40.000', 2);
INSERT INTO skyroute_db.ventas
(id_venta, id_cliente, id_destino, fecha_venta, id_estado)
VALUES(6, 3, 6, '2025-06-08 18:16:36.000', 3);

-- Insertar datos de prueba en Botón de Arrepentimiento
INSERT INTO skyroute_db.boton_arrepentimiento
(id_arrepentimiento, id_venta, id_cliente, id_destino, fecha_venta, fecha_arrepentimiento, id_estado)
VALUES(1, 3, 1, 4, '2025-06-08 17:13:41.000', '2025-06-08 17:13:48.000', 3);
INSERT INTO skyroute_db.boton_arrepentimiento
(id_arrepentimiento, id_venta, id_cliente, id_destino, fecha_venta, fecha_arrepentimiento, id_estado)
VALUES(2, 6, 3, 6, '2025-06-08 18:16:36.000', '2025-06-08 18:16:59.000', 3);
