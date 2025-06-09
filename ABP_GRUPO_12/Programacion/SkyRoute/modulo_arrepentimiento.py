from conexion_db import conectar
from datetime import datetime
from decimal import Decimal


# -------------Botón de arrepentimiento -------------------
#------------Función para Cancelar una venta --------------

def btn_arrepentimiento():

    conexion=conectar()
    cursor=conexion.cursor()

    id_sale = int(input("\nIngrese el código id de venta que desea cancelar: "))

    # Este código SQL permite buscar la venta que se quiere modificar con estado diferente de cancelada y que su registro sea menor a 60 dias(3 minutos)
    cursor.execute("""
    SELECT v.id_venta as Codigo_venta, c.DNI , c.nombre ,c.apellido, d.ciudad, d.estado , d.pais, d.costo_base_destino, e.nombre_estado ,v.fecha_venta
    FROM ventas v inner join cliente c on v.id_cliente=c.id_cliente inner join destinos d on v.id_destino=d.id_destino inner join estados e on v.id_estado=e.id_estado
    WHERE v.id_estado != 3 and v.fecha_venta >= NOW() - INTERVAL 3 MINUTE and v.id_venta = %s""", (id_sale,)) 
    sale = cursor.fetchone()

#Si existe la venta se muestra y se cancela, registrando en la tabla boton_arrepentimeinto
    if not sale:
        print("\n*************************************************************************************")
        print("\nLa venta ingresada no se encuentra disponible para cancelar *** código de venta ***: ", id_sale)
        print("\n*************************************************************************************")
        conexion.close()
        return 
    else:
        costo = float(sale[7]) if isinstance(sale[7], Decimal) else sale[7]
        fecha_venta = sale[9].strftime('%Y-%m-%d %H:%M:%S') if isinstance(sale[9], datetime) else sale[9]        
        print(f"""
************************************************************************
        Detalles de la venta a cancelar:
------------------------------------------------------------------------              
        ID: {sale[0]} | DNI: {sale[1]} | Nombre: {sale[2]} | Apellido: {sale[3]} 
        Ciudad: {sale[4]} | Provincia: {sale[5]} | País: {sale[6]}
        Costo: $ {costo:.2f} | Estado: {sale[8]} | Fecha de Venta: {fecha_venta}
        """)
#se asigna el valor 3 = CENACELADO a la varible state_sale para luego cancelar la venta 
        state_sale= 3
        fecha_actual = datetime.now()

        cursor.execute("""
                UPDATE ventas
                SET  id_estado= %s
                WHERE id_venta = %s 
                """, (state_sale, id_sale))

        conexion.commit()

        cursor.execute("""
                SELECT v.id_venta, c.id_cliente, d.id_destino, v.fecha_venta
                FROM ventas v
                INNER JOIN cliente c ON v.id_cliente=c.id_cliente 
                INNER JOIN destinos d ON v.id_destino=d.id_destino
                WHERE v.id_venta = %s
                """, (id_sale,))
        info = cursor.fetchone()

        if not info:
            print("Error al obtener los datos necesarios para el registro del arrepentimiento.")
            conexion.close()
            return

        id_venta = info[0]
        id_cliente = info[1]
        id_destino = info[2]
        fecha_venta = info[3]


        cursor.execute("""
                INSERT INTO boton_arrepentimiento (id_venta,id_cliente,id_destino,fecha_venta,fecha_arrepentimiento,id_estado)
                VALUES( %s,%s, %s,%s ,%s,%s)
                """, (id_venta, id_cliente, id_destino, fecha_venta, fecha_actual, state_sale))

        conexion.commit()

#+++Agregar los datos para que se muestre la venta cancelada.+++
    # Este código SQL permite buscar la venta que se quiere modificar
        cursor.execute("""
            SELECT v.id_venta as Codigo_venta, c.DNI , c.nombre ,c.apellido, d.ciudad, d.estado , d.pais, d.costo_base_destino, e.nombre_estado ,v.fecha_venta , ba.fecha_arrepentimiento
            FROM ventas v inner join cliente c on v.id_cliente=c.id_cliente inner join destinos d on v.id_destino=d.id_destino inner join estados e on v.id_estado=e.id_estado
            inner join boton_arrepentimiento ba on v.id_venta=ba.id_venta
            WHERE v.id_venta = %s""", (id_sale,)) 

        cancelada = cursor.fetchone()

        if cancelada:
            print("\n*********************************************")
            print("\nLa venta fue cancelada exitosamente: ")
  
            print(f"""
************************************************************************
        Detalles de la venta cancelada:
------------------------------------------------------------------                  
                  
                  ID: {cancelada[0]} | DNI: {cancelada[1]} | Nombre: {cancelada[2]} | Apellido: {cancelada[3]} | 
                  Ciudad Destino: {cancelada[4]} | Provincia Destino: {cancelada[5]} | País Destino: {cancelada[6]} | Costo: $ {cancelada[7]} | 
                  Estado Venta: {cancelada[8]}| Fecha de venta: {cancelada[9]} | Fecha de arrepentimiento: {cancelada[10]}
""")
        else:

            print("ooops parece que hubo un error por favor contacte el administrador.")

    conexion.close()

