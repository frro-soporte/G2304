"""Base de Datos SQL - Modificación"""

import datetime

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    """Implementar la funcion actualizar_persona, que actualiza un registro de
    una persona basado en su id. Devuelve un booleano en base a si encontro el
    registro y lo actualizo o no."""

    conexion = sqlite3.connect("practico_04_database.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE persona SET nombre = ?, fechaNacimiento = ?, dni = ?, altura = ? WHERE idPersona = ?", (nombre, nacimiento, dni, altura, id_persona))
    filasModificadas = cursor.rowcount
    conexion.commit()
    conexion.close()
    if filasModificadas != 0:
      return True
    
    return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', '1988-05-15', 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', '1988-04-16', 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', '1988-04-16', 32165497, 181)
    assert actualizar_persona(123, 'nadie', '1988-04-16', 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
