


from conexion_db import conectar


#---------------función crear clientes----------------------

def registrar_clientes ():
    conexion=conectar()
    cursor=conexion.cursor()

    dni = int(input("Ingrese DNI de contacto: "))
    cuit_cuil = input("Ingrese CUIT o CUIL del contacto: ")
    nombre = input("Ingrese NOMBRE de contacto: ")
    apellido = input("Ingrese APELLIDO de contacto: ")
    razon_social=(input("Ingrese RAZÓN SOCIAL: "))
    correo = input("Ingrese CORREO de contacto: ")
    telefono= input("Ingrese TELÉFONO de contacto: ")

    print("Tipo de persona:")
    print("1. Persona física")
    print("2. Persona jurídica")
    
    tipo_de_cliente= int(input("Si es una empresa ingrese 1 si es particular ingrese 2: "))

#si el usuario no ingresa un valor valido se definira que el cliente es una persona física

    if tipo_de_cliente not in [1, 2]:
        tipo_de_cliente = 1

#Acá hay código SQL: para insertar clientes

    cursor.execute("""
        INSERT INTO cliente ( DNI, CUIT_CUIL, nombre, apellido, razon_social, email, telefono,id_tipo_persona) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (dni, cuit_cuil, nombre, apellido, razon_social, correo, telefono,tipo_de_cliente))
    
    conexion.commit()
    conexion.close()

    print("\nCliente agregado exitosamente.")

    print(f"""

************************************************************************
        Detalles del Cliente:
------------------------------------------------------------------

        DNI: {dni} , 
        CUIT/CUIL: {cuit_cuil} , 
        Nombre: {nombre} , 
        Apellido: {apellido}, 
        Razón Social {razon_social} , 
        Correo: {correo} , 
        Teléfono: {telefono}, 
        Tipo de Cliente: {tipo_de_cliente} """)
    
#-------------Función para listar clientes------------------------------

def listar_clientes():
    conexion=conectar()
    cursor=conexion.cursor()

#Acá hay código SQL para consultar clientes

    cursor.execute("""
    SELECT c.id_cliente, c.nombre, c.apellido, c.razon_social,  c.email, tp.descripcion
    FROM cliente c
    LEFT JOIN tipo_persona tp ON c.id_tipo_persona = tp.id_tipo_persona
    """)
    resultados_clientes = cursor.fetchall()

    if resultados_clientes:
        print("\nLista de Clientes: ")
  
        for var_cl in resultados_clientes:
            print(f"ID: {var_cl[0]} | Nombre: {var_cl[1]} {var_cl[2]} | Razón Social: {var_cl[3]} | Email: {var_cl[4]} | Tipo: {var_cl[5]}")

    else:
        print("La lista de clientes está vacía.")

    conexion.close()

#--------------------Función eliminar clientes------------------------

def eliminar_cliente():

    conexion=conectar()
    cursor=conexion.cursor()

    dni = int(input("Ingrese el DNI del cliente a eliminar: "))
   
   
#Acá hay código SQL para borrar clientes
    cursor.execute("DELETE FROM cliente WHERE DNI = %s", (dni,))

    if cursor.rowcount > 0:
        print("************************************************************************")
        print(f"El Cliente:  {dni} ha sido eliminado.")
        print("************************************************************************")
    else:
        print("************************************************************************")
        print(f"No se encontró el cliente  {dni}.")
        print("************************************************************************")

    conexion.commit()
    conexion.close()


#----------------Modificar clientes---------------------------

def modificar_clientes():

    conexion=conectar()
    cursor=conexion.cursor()

    dni = input("Ingrese el DNI del cliente que desea modificar: ")
    cursor.execute("SELECT * FROM cliente WHERE dni = %s", (dni,)) #Acá hay código SQL
    persona = cursor.fetchone()

    if persona:
            print("Datos actuales del cliente:", persona)
            doc= int(input("Ingrese el nuevo documento: "))
            cuit_cuil= input("Ingrese el nuevo cuit o cuil: ")
            apellido = input("Ingrese el nuevo apellido: ")
            nombre = input("Ingrese el nuevo nombre: ")
            razon_social = input("Ingrese la nueva razón social: ")
            email = input("Ingrese el nuevo email: ")
            telefono = input("Ingrese el nuevo número de teléfono: ")
            print("Tipo de persona:")
            print("1. Persona física")
            print("2. Persona jurídica")
    
            tipo_de_cliente= int(input("Si es una empresa ingrese 1 si es particular ingrese 2: "))

            #si el usuario no ingresa un valor valido se definira que el cliente es una persona física

            if tipo_de_cliente not in [1, 2]:
                tipo_de_cliente = 1

            #Acá hay código SQL
            cursor.execute("""
            UPDATE cliente
            SET DNI= %s , CUIT_CUIL= %s , nombre= %s, apellido= %s, razon_social= %s, email= %s, telefono= %s,id_tipo_persona= %s
            WHERE dni = %s
            """, (doc, cuit_cuil, nombre, apellido, razon_social, email, telefono,tipo_de_cliente,dni ))

            conexion.commit()
            print("************************************************************************")
            print("Cliente modificado exitosamente.")



            print(f"""

************************************************************************
        Detalles del Cliente:
------------------------------------------------------------------

        DNI: {doc} , 
        CUIT/CUIL: {cuit_cuil} , 
        Nombre: {nombre} , 
        Apellido: {apellido}, 
        Razón Social {razon_social} , 
        Correo: {email} , 
        Teléfono: {telefono}, 
        Tipo de Cliente: {tipo_de_cliente} """)
            print("************************************************************************")
    else:
        print("************************************************************************")
        print("No se encontró ningun cliente con ese DNI.")
        print("************************************************************************")
    conexion.close()