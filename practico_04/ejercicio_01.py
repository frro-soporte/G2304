"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    conexion = sqlite3.connect("practico_04_database.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS persona(idPersona INTEGER PRIMARY KEY, nombre CHAR(30), fechaNacimiento DATE, dni INTEGER, altura INTEGER)")
    conexion.commit()
    conexion.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
   conexion = sqlite3.connect("practico_04_database.db")
   cursor = conexion.cursor()
   cursor.execute("DELETE FROM persona")
   conexion.commit()
   conexion.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
