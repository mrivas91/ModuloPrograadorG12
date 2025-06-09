-- Consultas SQL útiles
-- DML | Consultas y/o recuperación de datos.

-- 1. Listar todos los clientes
    SELECT c.id_cliente, c.nombre, c.apellido, c.razon_social,  c.email, tp.descripcion
    FROM cliente c
    LEFT JOIN tipo_persona tp ON c.id_tipo_persona = tp.id_tipo_persona

-- 2. Mostrar las ventas realizadas entre en la ultima semana.

    SELECT v.id_venta as Codigo_venta, c.DNI , c.nombre ,c.apellido, d.ciudad, d.estado , d.pais, d.costo_base_destino, e.nombre_estado 
    FROM ventas v inner join cliente c on v.id_cliente=c.id_cliente inner join destinos d on v.id_destino=d.id_destino 
    inner join estados e on v.id_estado=e.id_estado
    WHERE v.fecha_venta >= CURDATE() - INTERVAL 7 DAY;

-- 3. Obtener la última venta de cada cliente.

SELECT c.nombre   AS Nombre_cliente, c.apellido AS Apellido_cliente, c.id_cliente, MAX(v.fecha_venta) AS ultima_venta 
FROM ventas v 
JOIN cliente c ON v.id_cliente = c.id_cliente 
GROUP BY v.id_cliente, c.razon_social;

-- 4. Listar todos los destinos que comienzan con "L".

SELECT id_destino,pais,estado,ciudad,costo_base_destino
FROM destinos
WHERE ciudad LIKE 'L%'

-- 5. Mostrar cuántas ventas se realizaron por país.

SELECT d.pais, COUNT(v.id_venta) AS total_ventas 
FROM Ventas v 
JOIN destinos d ON v.id_destino = d.id_destino
GROUP BY d.pais 
ORDER BY total_ventas DESC; 

-- 6. Cantidad de ventas por cliente y destino.

SELECT c.nombre AS Nombre_Cliente,c.apellido as apellido_cliente, d.ciudad AS Destino, d.pais AS País, COUNT(v.id_venta) AS Total_Ventas  -- Selección de campos, 
FROM Ventas v  -- Especifica desde qué tabla se traen los datos, asignación de alias v.
JOIN Cliente c ON v.id_cliente = c.id_cliente -- Unión de tablar por campo id_cliente.
JOIN Destinos d ON v.id_destino = d.id_destino -- Unión de tablar por campo id_destino.
GROUP BY c.razon_social, d.ciudad, d.pais -- Agrupación por campos, permite usar COUNT. 
ORDER BY Total_Ventas DESC; -- Ordena resultados de manera descendente según el total de ventas.

-- 7. Mostrar todas las ventas anuladas mediante el Botón de Arrepentimiento

SELECT v.id_venta as Codigo_venta, c.DNI , c.nombre ,c.apellido, d.ciudad, d.estado , d.pais, d.costo_base_destino, e.nombre_estado ,v.fecha_venta , ba.fecha_arrepentimiento
FROM ventas v inner join cliente c on v.id_cliente=c.id_cliente inner join destinos d on v.id_destino=d.id_destino inner join estados e on v.id_estado=e.id_estado
inner join boton_arrepentimiento ba on v.id_venta=ba.id_venta