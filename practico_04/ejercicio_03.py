"""Base de Datos SQL - Baja"""

import datetime

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    conexion = sqlite3.connect("practico_04_database.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM persona WHERE idPersona = ?",(id_persona, ))
    per = cursor.fetchone()
    cursor.execute("DELETE FROM persona WHERE idPersona = ?", (id_persona, ))
    filasModificadas = cursor.rowcount
    conexion.commit()
    conexion.close()
    if per != None and filasModificadas != 0:
      return True
    
    return False




  # NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', '1988-05-15', 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
