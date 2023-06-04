"""Base de Datos SQL - Alta"""

import datetime
from practico_04.ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la funcion agregar_persona, que inserte un registro en la 
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""
    conexion = sqlite3.connect("practico_04_database.db")
    cursor = conexion.cursor()
    contador = cursor.lastrowid
    cursor.execute("INSERT INTO persona VALUES(?,?,?,?,?)",(contador, nombre, nacimiento, dni, altura))
    id = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return id



# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', '1988-05-12', 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', '1980-01-25', 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
