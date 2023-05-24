"""Base de Datos SQL - Búsqueda"""

import datetime

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    conexion = sqlite3.connect("practico_04_database.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM persona WHERE idPersona = ?",(id_persona, ))
    per = cursor.fetchone()
    conexion.commit()
    conexion.close()

    if per != None:
      return per
    
    return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', "15/05/1988", 32165498, 180))
    assert juan == (1, 'juan perez', "15/05/1988", 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
