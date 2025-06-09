

from conexion_db import conectar

#----función crear nuevo destino------

def registrar_destino ():
    conexion=conectar()
    cursor=conexion.cursor()

    print("************************************************************************")
    pais=input("Ingrese el nombre del PAIS de destino: ")
    estado=input("Ingrese el nombre del ESTADO de destino: ")
    ciudad=input("Ingrese el nombre de la CIUDAD de destino: ")
    costo_destino=float(input("Ingrese el COSTO de destino: $"))

#Acá hay código SQL: para insertar destinos

    cursor.execute("""
        INSERT INTO destinos ( pais,estado,ciudad,costo_base_destino) 
        VALUES ( %s, %s, %s, %s)
        """, (pais,estado,ciudad,costo_destino))
    
    conexion.commit()
    conexion.close()  

    print("************************************************************************")
    print("\nEl destino fue agregado exitosamente.")

    print(f"""

************************************************************************
        Detalles del Destino:
------------------------------------------------------------------

        País: {pais} , 
        Estado: {estado} , 
        Ciudad: {ciudad} , 
        Costo destino: $ {float(costo_destino):.2f}
    """)  
#-------Función para listar destinos----------

def listar_destinos():
    conexion=conectar()
    cursor=conexion.cursor()

#Acá hay código SQL para consultar destinos

    cursor.execute("""
    SELECT id_destino,pais,estado,ciudad,costo_base_destino
    FROM destinos
    """)
    resultados_destinos = cursor.fetchall()

    if resultados_destinos:
        print("************************************************************************")
        print("\nLista de Destinos: ")
  
        for var_des in resultados_destinos:
            print(f"ID: {var_des[0]} | País: {var_des[1]} | Estado: {var_des[2]} | Ciudad: {var_des[3]} | Costo: $ {var_des[4]}")

    else:
        print("************************************************************************")
        print("La lista de destinos está vacía.")
        print("************************************************************************")

    conexion.close()

#---------Función eliminar destinos--------------

def eliminar_destino():

    conexion=conectar()
    cursor=conexion.cursor()

    ciudad = input("Ingrese el nombre de la ciudad a eliminar: ")
   
   
#Acá hay código SQL para borrar destino
    cursor.execute("DELETE FROM destinos WHERE ciudad LIKE %s", (f"%{ciudad}%",))

    if cursor.rowcount > 0:
        print("************************************************************************")
        print(f"El destino:  {ciudad} ha sido eliminado.")
        print("************************************************************************")
    else:
        print(f"No se encontró la ciudad: {ciudad}.")

    conexion.commit()
    conexion.close()

#------------Función para modificar un destino--------------

def modificar_destino():

    conexion=conectar()
    cursor=conexion.cursor()

    id = int(input("Ingrese el código id de destino que desea modificar: "))
    cursor.execute("SELECT * FROM destinos WHERE id_destino = %s", (id,)) #Acá hay código SQL
    lugar = cursor.fetchone()

    if lugar:
        print("Datos actuales del destino:", lugar)
        pais=input("Ingrese el nombre del PAIS de destino: ")
        estado=input("Ingrese el nombre del ESTADO de destino: ")
        ciudad=input("Ingrese el nombre de la CIUDAD de destino: ")
        costo_destino=float(input("Ingrese el COSTO de destino: $"))

            #Acá hay código SQL-- sentencia update para modificar destino
        cursor.execute("""
        UPDATE destinos
        SET  pais= %s,estado= %s,ciudad= %s,costo_base_destino= %s
        WHERE id_destino = %s 
        """, (  pais,estado,ciudad,costo_destino, id))

        conexion.commit()
        print("************************************************************************")
        print("El destino fue modificado exitosamente.")
        print("************************************************************************")
        print(f"""

************************************************************************
        Detalles del Destino:
------------------------------------------------------------------

        País: {pais} , 
        Estado: {estado} , 
        Ciudad: {ciudad} , 
        Costo destino: $ {float(costo_destino):.2f}
    """) 
    else:
        print("************************************************************************")
        print("No se encontró ningun destino con esa ciudad.")
        print("************************************************************************")
        conexion.close()
