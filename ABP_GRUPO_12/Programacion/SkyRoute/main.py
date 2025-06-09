# SkyRoute S.R.L. - Sistema de Gestión de Pasajes
# Propósito: Prototipo de aplicación de consola para la gestión de pasajes aéreos.
# Instalación y ejecución: Ejecutar con Python desde la terminal.


from conexion_db import crear_base_datos, crear_tabla_si_no_existe, conectar
import conexion_db
import modulo_clientes
import modulo_destinos
import modulo_ventas
import modulo_arrepentimiento



def main():
    while True:
        print("\nTe damos la bienvenida a SkyRoute - Sistema de Gestión de Pasajes")
        print("1. Gestionar Clientes")
        print("2. Gestionar Destinos")
        print("3. Gestionar Ventas")
        print("4. Consultar Ventas")
        print("5. Botón de Arrepentimiento")
        print("6. Ver Reporte General")
        print("7. Acerca del Sistema")
        print("8. Salir")


        opcion = input("\nSeleccione una opción: ")


        if opcion == "1":
            print("\nIngreso a la opción: Gestionar Clientes")
            print("\n-- GESTIONAR CLIENTES --")
            print("1. Ver Clientes")
            print("2. Agregar Cliente")
            print("3. Modificar Cliente")
            print("4. Eliminar Cliente")
            print("5. Volver al Menú Principal")


            opcion_clientes = input("\nSeleccione una opción: ")


            if opcion_clientes == "1":
                print("\nSeleccionó la opción Ver Clientes")                
                modulo_clientes.listar_clientes()
            elif opcion_clientes == "2":
                print("\nSeleccionó la opción Agregar Clientes")   
                modulo_clientes.registrar_clientes()
            elif opcion_clientes == "3":
                print("\nSeleccionó Modificar un cliente.")
                modulo_clientes.modificar_clientes()
            elif opcion_clientes == "4":
                print("\nSeleccionó Eliminar un cliente.")
                modulo_clientes.eliminar_cliente()
            elif opcion_clientes == "5":
                print("\nSeleccionó Volver al menú principal.")
            else:
                print("\nOpción no válida. Intente nuevamente.")


        elif opcion == "2":
            print("\nIngreso a la opción: Gestionar Destinos")
            print("\n-- GESTIONAR DESTINOS --")
            print("1. Ver Destinos")
            print("2. Agregar Destino")
            print("3. Modificar Destino")
            print("4. Eliminar Destino")
            print("5. Volver al Menú Principal")


            opcion_destinos = input("\nSeleccione una opción: ")


            if opcion_destinos == "1":
                print("\nSeleccionó Ver destinos")
                modulo_destinos.listar_destinos()
            elif opcion_destinos == "2":
                print("\nSeleccionó Agregar un destino")
                modulo_destinos.registrar_destino()
            elif opcion_destinos == "3":
                print("\nSeleccionó Modificar un destino.")
                modulo_destinos.modificar_destino()
            elif opcion_destinos == "4":
                print("\nSeleccionó Eliminar un destino.")
                modulo_destinos.eliminar_destino()
            elif opcion_destinos == "5":
                print("\nSeleccionó Volver al menú principal.")
            else:
                print("\nOpción no válida. Intente nuevamente.")


        elif opcion == "3":
            print("\nIngreso a la opción: Gestionar Ventas")
            print("\n-- GESTIONAR VENTAS --")
            print("1. Registrar Venta")
            print("2. Modificar Venta")
            print("3. Eliminar Venta")
            print("4. Confirmar Venta")
            print("5. Volver al Menú Principal")


            opcion_ventas = input("\nSeleccione una opción: ")


            if opcion_ventas == "1":
                print("\nSeleccionó Registrar una venta.")
                modulo_ventas.registrar_venta()
            elif opcion_ventas == "2":
                print("\nSeleccionó Modificar una venta.")
                modulo_ventas.modificar_venta()
            elif opcion_ventas == "3":
                print("\nSeleccionó Eliminar una venta.")
                modulo_ventas.eliminar_venta()
            elif opcion_ventas=="4":
                print("\nSeleccionó Confirmar una venta.")
                modulo_ventas.confirmar_venta()
            elif opcion_ventas == "5":
                print("\nSeleccionó Volver al menú principal.")
            else:
                print("\nOpción no válida. Intente nuevamente.")


        elif opcion == "4":
            print("\nIngreso a la opción: Consultar Ventas")
            print("\n-- CONSULTAR VENTAS --")
            print("1. Ver todas las ventas")
            print("2. Filtrar por cliente")
            print("3. Ventas de la última semana")
            print("4. Volver al Menú Principal")


            opcion_consulta = input("\nSeleccione una opción: ")


            if opcion_consulta == "1":
                print("\nSeleccionó ver todas las ventas.")
                modulo_ventas.listar_ventas()
            elif opcion_consulta == "2":
                print("\nSeleccionó ver las ventas filtradas por cliente.")
                modulo_ventas.listar_ventas_cliente()
            elif opcion_consulta == "3":
                print("\nSeleccionó ver las ventas de la última semana.")
                modulo_ventas.listar_ventas_ultima_semana()
            elif opcion_consulta == "4":
                print("\nSeleccionó Volver al menú principal.")
            else:
                print("\nOpción no válida. Intente nuevamente.")


        elif opcion == "5":
            print("\n*********************************************")
            print("\nIngreso a la opción: Botón de Arrepentimiento")
            print("\n*********************************************")
            modulo_arrepentimiento.btn_arrepentimiento()


        elif opcion == "6":
            print("\n*********************************************")
            print("\nIngreso a la opción: Ver Reporte General")
            print("Mostrando el reporte de todas las operaciones realizadas.")
            print("\n*********************************************")
            modulo_ventas.listar_ventas()


        elif opcion == "7":
            print("\n--------------Ingreso a la opción: Acerca del Sistema------------")
            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\n*SkyRoute S.R.L. - Sistema de Gestión de Pasajes Aéreos")
            print("\n*Versión 2.0 - Prototipo de consola desarrollado por estudiantes de ISPC.")
            print( """\n# Proyecto: Sistema de gestión de pasajes - SkyRoute S.R.L.
# Autor: 
 [Integrantes]:
 * Avila, Daniela Carolina:36706615
 * Fava Perez, Maria Pia: 30722626
 * Rivas, Mariela Yanina: 34677549
 * Raspanti, Gerardo: 35524770 
 
*Derechos reservados. Prohibida la distribución sin permiso del autor.""")
            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        elif opcion == "8":
            print("\n*********************************************")
            print("\nGracias por usar SkyRoute. ¡Hasta pronto!")
            print("\n*********************************************")
            break


        else:
            print("\nOpción no válida. Por favor, intente nuevamente.")


# Inicialización del sistema
crear_base_datos()
conexion = conexion_db.conectar()
crear_tabla_si_no_existe(conexion)
conexion.close()

# Verificamos si este archivo se ejecuta directamente (no importado)
if __name__ == "__main__":
    main()