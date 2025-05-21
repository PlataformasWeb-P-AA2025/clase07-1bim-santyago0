from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Sacar las matriculas con su estudiante y módulo
matriculas = session.query(Matricula).all()

#for m in matriculas:
#    print(m, m.estudiante, m.modulo)

# Obtener todos los módulos que tengan matrículas de estudiantes cuyo nombre sea Tony
# Para esta consulta debemos hacer un Join con Matrículas, que es la clase que relaciona los módulos y los estudiantes
# después otro Join con Estudiantes, ya que de aquí vamos a poder filtrar los estudiantes con el nombres Tony
modulos = session.query(Modulo).join(Matricula).join(Estudiante).\
    filter(Estudiante.nombre == "Tony").all()
print(modulos)
