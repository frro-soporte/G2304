"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio

from typing import List, Optional

class DatosSocio():
        
        def __init__(self):
            pass # Completar
            engine = create_engine('sqlite:///socios.db', echo = True)
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind = engine)
            self.session = Session()
        
        def buscar(self, id_socio: int) -> Optional[Socio]:
            """Devuelve la instancia del socio, dado su id. Devuelve None si no 
            encuentra nada.
            """
            try:
                socio = self.session.query(Socio).filter_by(id_socio=id_socio).first()
                return socio
            except:
                raise Exception("Error al buscar el socio en la base de datos")
                 
        
        def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
            """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
            encuentra nada.
            """
            #pass # Completar
    
            try:
                socio = self.session.query(Socio).filter_by(dni=dni_socio).first()
                return socio
            except:
                raise Exception("Error al buscar el socio en la base de datos")
        
        def todos(self) -> List[Socio]:
            """Devuelve listado de todos los socios en la base de datos."""
            pass # Completar
            socios = self.session.query(Socio).all()
            return socios
        
        def borrar_todos(self) -> bool:
            """Borra todos los socios de la base de datos. Devuelve True si el 
            borrado fue exitoso.
            """
            pass # Completar
            
            self.session.query(Socio).delete()
            self.session.commit()
            if socio is None:
                 return True
            else:
                return False
        
        def alta(self, socio: Socio) -> Socio:
            """Agrega un nuevo socio a la tabla y lo devuelve"""
            #pass # Completar
            socio_encontrado = self.buscar_dni(socio.dni)
            if socio_encontrado is None:
                self.session.add(socio)
                self.session.commit()
                return socio
            else: 
               print('Socio ya registrado')
            
        def baja(self, id_socio: int) -> bool:
            """Borra el socio especificado por el id. Devuelve True si el borrado 
            fue exitoso.
            """
            pass # Completar
            socio = self.buscar(id_socio)
            try:
                self.session.delete(socio)
                self.session.commit()
                return True
            except:
                self.session.rollback()
                return False
        

        def modificacion(self, socio: Socio) -> Socio:
            """Guarda un socio con sus datos modificados. Devuelve el Socio 
            modificado.
            """
            pass # Completar
            self.session.query(Socio).filter_by(id_socio=socio.id_socio).update({
            Socio.nombre: socio.nombre,
            Socio.apellido: socio.apellido,
            Socio.dni: socio.dni})
            self.session.commit()
            return socio
        
        def contarSocios(self) -> int:
            """Devuelve el total de socios que existen en la tabla"""
            pass # Completar
            total_socios = self.session.query(Socio).count()
            return total_socios



# NO MODIFICAR - INICIO

# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id_socio > 0

# Test Baja
assert datos.baja(socio.id_socio) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id_socio) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id_socio)
assert socio_3_modificado.id_socio == socio_3.id_socio
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587

# Test Conteo
assert len(datos.todos()) == 3
print(datos.todos())
# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN