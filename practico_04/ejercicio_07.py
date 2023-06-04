"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime

from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

    per = buscar_persona(id_persona)
    
    if per:
      conexion = sqlite3.connect("practico_04_database.db")
      cursor = conexion.cursor()
      cursor.execute("SELECT fecha FROM PersonaPeso WHERE idPersona = ?", (id_persona, ))
      registro = cursor.fetchone()
      if registro == None:
        cursor.execute("INSERT INTO PersonaPeso (fecha, peso, idPersona) VALUES (?, ?, ?)", (fecha, peso, id_persona))
        filaInsertada = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return filaInsertada
      else:
        fechaRegistro = datetime.strptime(registro[0], '%Y-%m-%d')
        fechaParametro = datetime.strptime(fecha, '%Y-%m-%d')
        if fechaParametro > fechaRegistro:
            cursor.execute("INSERT INTO PersonaPeso (fecha, peso, idPersona) VALUES (?, ?, ?) ", (fecha, peso, id_persona))
            filaInsertada = cursor.lastrowid
            conexion.commit()
            conexion.close()
            return filaInsertada
      
    return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', '1988-05-15', 32165498, 180)
    assert agregar_peso(id_juan, '2018-05-26', 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, '1988-05-15', 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, '2018-05-16', 80) == False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
