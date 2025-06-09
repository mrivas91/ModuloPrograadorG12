

from conexion_db import conectar
from datetime import datetime

#----función crear una nueva venta------

def registrar_venta ():
    conexion=conectar()
    cursor=conexion.cursor()

    dni=int(input("Ingrese el nombre DNI del cliente: "))
    ciudad=input("Ingrese el nombre de la CIUDAD de destino: ")

#Acá hay código SQL: para buscar un  cliente
       # Buscar ID del cliente
    cursor.execute("SELECT id_cliente , nombre, apellido FROM  cliente WHERE DNI = %s", (dni,))
    resultado_cliente = cursor.fetchone()

    if not resultado_cliente:
        print("Cliente no encontrado.")

        conexion.close()
        return
    
    id_cliente, nombre_cliente, apellido_cliente = resultado_cliente

#Acá hay código SQL: para buscar destino

    # Buscar ID del destino
    cursor.execute("SELECT id_destino  , ciudad, estado, pais, costo_base_destino FROM destinos WHERE ciudad LIKE %s", (f"%{ciudad}%",))
    resultado_destino = cursor.fetchone()

    if not resultado_destino:
        print("Ciudad no encontrada.")

        conexion.close()
        return
    
    id_destino, ciudad_destino, estado_destino, pais_destino, costo_base = resultado_destino

    # Insertar la venta con estado pendiente
    fecha_actual = datetime.now()
    id_estado = 2  

#Acá hay código SQL: para insertar ventas 
    cursor.execute("""
        INSERT INTO ventas (id_cliente, id_destino, fecha_venta, id_estado)
        VALUES (%s, %s, %s, %s)
    """, (id_cliente, id_destino, fecha_actual, id_estado))

    conexion.commit()
    conexion.close()

    print("Ha registrado la venta exitosamente.")

    print(f"""
************************************************************************
          Detalles de la Venta:
------------------------------------------------------------------
    DNI Cliente       : {dni}
    Nombre Completo   : {nombre_cliente} {apellido_cliente}
    Destino           : {ciudad_destino}, {estado_destino}, {pais_destino}
    Costo             : $ {float(costo_base):.2f}
    Estado            : PENDIENTE
    Fecha de Venta    : {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}
    """)

  
#-------Función para listar ventas----------

def listar_ventas():
    conexion=conectar()
    cursor=conexion.cursor()

#Acá hay código SQL para consultar ventas

    cursor.execute("""
    SELECT v.id_venta as Codigo_venta, c.DNI , c.nombre ,c.apellido, d.ciudad, d.estado , d.pais, d.costo_base_destino, e.nombre_estado 
    FROM ventas v inner join cliente c on v.id_cliente=c.id_cliente inner join destinos d on v.id_destino=d.id_destino inner join estados e on v.id_estado=e.id_estado
    Order by v.id_venta asc;
    """)
    resultados_ventas = cursor.fetchall()

    if resultados_ventas:
        print("\nLista de ventas de pasajes: ")
  
        for var_des in resultados_ventas:
            print(f"ID: {var_des[0]} | DNI: {var_des[1]} | Nombre: {var_des[2]} | Apellido: {var_des[3]} | Ciudad Destino: {var_des[4]} | Provincia Destino: {var_des[5]} | País Destino: {var_des[6]} | Costo: $ {var_des[7]} | Estado Venta: $ {var_des[8]}")

    else:
        print("\nLa lista de ventas está vacía.")

    conexion.close()

#-------Función para listar ventas filtrada por clientes----------

def listar_ventas_cliente():
    conexion=conectar()
    cursor=conexion.cursor()

#Acá hay código SQL para consultar ventas

    dni=int(input("\nIngrese el nombre DNI del cliente: "))
    cursor.execute("""
    SELECT v.id_venta as Codigo_venta, c.DNI , c.nombre ,c.apellido, d.ciudad, d.estado , d.pais, d.costo_base_destino, e.nombre_estado 
    FROM ventas v inner join cliente c on v.id_cliente=c.id_cliente inner join destinos d on v.id_destino=d.id_destino inner join estados e on v.id_estado=e.id_estado
    WHERE c.DNI=%s
    Order by v.id_venta asc;
    """,(dni,))

    resultados_ventas = cursor.fetchall()

    if resultados_ventas:
        print("\nLista de ventas de pasajes poer cliente: ")
  
        for var_des in resultados_ventas:
            print(f"ID: {var_des[0]} | DNI: {var_des[1]} | Nombre: {var_des[2]} | Apellido: {var_des[3]} | Ciudad Destino: {var_des[4]} | Provincia Destino: {var_des[5]} | País Destino: {var_des[6]} | Costo: $ {var_des[7]} | Estado Venta: $ {var_des[8]} ")

    else:
        print("La lista de ventas está vacía.")

    conexion.close()

#-------Función para listar ventas ultima semana----------

def listar_ventas_ultima_semana():
    conexion=conectar()
    cursor=conexion.cursor()

#Acá hay código SQL para consultar ventas

    cursor.execute("""
    SELECT v.id_venta as Codigo_venta, c.DNI , c.nombre ,c.apellido, d.ciudad, d.estado , d.pais, d.costo_base_destino, e.nombre_estado 
    FROM ventas v inner join cliente c on v.id_cliente=c.id_cliente inner join destinos d on v.id_destino=d.id_destino inner join estados e on v.id_estado=e.id_estado
    WHERE v.fecha_venta >= CURDATE() - INTERVAL 7 DAY;
    """)
    resultados_ventas = cursor.fetchall()

    if resultados_ventas:
        print("\nLista de ventas de pasajes de la ultima semana: ")
  
        for var_des in resultados_ventas:
            print(f"ID: {var_des[0]} | DNI: {var_des[1]} | Nombre: {var_des[2]} | Apellido: {var_des[3]} | Ciudad Destino: {var_des[4]} | Provincia Destino: {var_des[5]} | País Destino: {var_des[6]} | Costo: $ {var_des[7]} | Estado Venta: $ {var_des[8]} ")
    else:
        print("\nLa no hay ventas en la ultima semana.")

    conexion.close()

#---------Función eliminar venta--------------

def eliminar_venta():

    conexion=conectar()
    cursor=conexion.cursor()

    id_sale = int(input("Ingrese código de venta a eliminar: "))
   
   
#Acá hay código SQL para borrar ventas
    cursor.execute("DELETE FROM ventas WHERE id_venta= %s", (id_sale,))

    if cursor.rowcount > 0:
        print(f"La venta:  {id_sale} ha sido eliminada.")
    else:
        print(f"No se encontró la venta: {id_sale}.")

    conexion.commit()
    conexion.close()

#------------Función para modificar una venta--------------

def modificar_venta():

    conexion=conectar()
    cursor=conexion.cursor()

    id_sale = int(input("Ingrese el código id de venta que desea modificar: "))

    # Este código SQL permite buscar la venta que se quiere modificar
    cursor.execute("""
    SELECT v.id_venta as Codigo_venta, c.DNI , c.nombre ,c.apellido, d.ciudad, d.estado , d.pais, d.costo_base_destino, e.nombre_estado 
    FROM ventas v inner join cliente c on v.id_cliente=c.id_cliente inner join destinos d on v.id_destino=d.id_destino inner join estados e on v.id_estado=e.id_estado
    WHERE id_venta = %s""", (id_sale,)) 
    sale = cursor.fetchone()

#Si existe la venta se muestra y solicita ingreso de nuevos valores
    if sale:
        print("Datos actuales de la venta:", sale)
        dni=int(input("Ingrese el número de DNI del cliente: "))
        ciudad=input("Ingrese el nombre de la CIUDAD de destino: ")

        print("Estado de la venta:")
        print("1. APROBADA")
        print("2. PENDIENTE")

    
        state_sale= int(input("Si es una venta APROBADA ingrese 1 y si es PENDIENTE ingrese 2: "))

#si el usuario no ingresa un valor valido se define que la venta esta PENDIENTE

        if state_sale not in [1, 2]:
            state_sale = 2

#Acá hay código SQL: para buscar un  cliente
       # Buscar ID del cliente
        cursor.execute("SELECT id_cliente FROM cliente WHERE DNI = %s", (dni,))
        resultado_cliente = cursor.fetchone()

        if not resultado_cliente:
            print("Cliente no encontrado.")

            conexion.close()
            return
    
        id_cliente = resultado_cliente[0]

#Acá hay código SQL: para insertar buscar destino

        # Buscar ID del destino
        cursor.execute("SELECT id_destino FROM destinos WHERE ciudad LIKE %s", (f"%{ciudad}%",))
        resultado_destino = cursor.fetchone()

        if not resultado_destino:
            print("Ciudad no encontrada.")

            conexion.close()
            return
    
        id_destino = resultado_destino[0]
        fecha_actual = datetime.now()

        cursor.execute("""
                UPDATE ventas
                SET  id_cliente= %s ,id_destino=  %s, fecha_venta=%s ,id_estado= %s
                WHERE id_venta = %s 
                """, (id_cliente,id_destino,fecha_actual, state_sale, id_sale))

        conexion.commit()

        print(f"""
************************************************************************
          Detalles de la Venta:
------------------------------------------------------------------------  
ID Venta: {id_sale}
Cliente DNI: {dni}
Ciudad destino: {ciudad}
Estado: {"APROBADA" if state_sale == 1 else "PENDIENTE"}
------------------------------------------------------------------------                  
""")

        print("\nLa venta fue modificada exitosamente.")
    else:
        print("\nNo se encontró ninguna venta con ese código.")
    conexion.close()

#------------Función para confirmar una venta--------------

def confirmar_venta():

    conexion=conectar()
    cursor=conexion.cursor()

    id_sale = int(input("Ingrese el código id de venta que desea confirmar: "))

    # Este código SQL permite buscar la venta que se quiere modificar
    cursor.execute("""
    SELECT v.id_venta as Codigo_venta, c.DNI , c.nombre ,c.apellido, d.ciudad, d.estado , d.pais, d.costo_base_destino, e.nombre_estado 
    FROM ventas v inner join cliente c on v.id_cliente=c.id_cliente inner join destinos d on v.id_destino=d.id_destino inner join estados e on v.id_estado=e.id_estado
    WHERE v.id_estado= 2 and v.id_venta = %s""", (id_sale,)) 
    sale = cursor.fetchone()

#Si existe la venta se muestra y solicita ingreso de nuevos valores
    if not sale:
        print("\nNo se encontró ninguna venta PENDIENTE con ese código: ", id_sale)
        conexion.close()
        return 
    else:
        print("Datos actuales de la venta:", sale)
#se asigna el valor 1 = APROBADO a la varible state_sale    
        state_sale= 1
        fecha_actual = datetime.now()

        cursor.execute("""
                UPDATE ventas
                SET  fecha_venta=%s ,id_estado= %s
                WHERE id_venta = %s 
                """, (fecha_actual, state_sale, id_sale))

        conexion.commit()

#+++Agregar los datos para que se muestre la venta confirmada.+++
    # Este código SQL permite buscar la venta que se quiere modificar
    cursor.execute("""
    SELECT v.id_venta as Codigo_venta, c.DNI , c.nombre ,c.apellido, d.ciudad, d.estado , d.pais, d.costo_base_destino, e.nombre_estado 
    FROM ventas v inner join cliente c on v.id_cliente=c.id_cliente inner join destinos d on v.id_destino=d.id_destino inner join estados e on v.id_estado=e.id_estado
    WHERE v.id_venta = %s""", (id_sale,)) 

    confirmada = cursor.fetchone()

    if confirmada:
        print("\nLa venta fue actualizada exitosamente: ")
  
        print(f"""
************************************************************************
          Detalles de la Venta:
------------------------------------------------------------------------                
              ID: {confirmada[0]} | DNI: {confirmada[1]} | Nombre: {confirmada[2]} | Apellido: {confirmada[3]} | Ciudad Destino: {confirmada[4]} | Provincia Destino: {confirmada[5]} | País Destino: {confirmada[6]} | Costo: $ {confirmada[7]} | Estado Venta: {confirmada[8]}
------------------------------------------------------------------------                  
""")
    else:

        print("\nOoops parece que hubo un error por favor contacte el administrador.")

    conexion.close()

