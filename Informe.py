### Sistema de gestión para una Clinica

"""
Este sistema orientado a objetos esta diseñado para gestionar informáticamente una clínica médica, 
donde podemos administrar la información de los pacientes y medicos, recetas, turnos, historias clinicas.
Las clases son:"""

# Clase Paciente:

"""Guardamos los datos personales de los pacientes, como DNI, nombre, apellido y fecha de nacimiento, 
verificando los datos que esten completos y sean correctos"""

# Clase Médico:

"""Guardamos sus datos personales, como DNI, nombre, apellido, matrícula y especialidad, 
permite que el medico agregue especialidades, tambien que atienda varios dias"""

#Clase Receta:

"""Esta clase simula una receta, que puede tener varios medicamentos y registra en que fecha fue emitida"""

#Clase Turno:

"""Esta clase simula un turno pedido por un paciente a un médico con cierta especialidad, 
con fecha y hora específicas. Verifica la veracidad de los datos, si el día del turno coincide con otro, 
obtener la fecha y hora, y mostrar el turno como una cadena legible"""

#Clase Especialidad:

"""Esta clase simula una especialidad médica como "Neurología" o "Dermatología" y los dias disponibles de cada especialidad. 
Verifica que los datos esten completos y sean válidos, si esa especialidad atiende cierto dia"""

#Clase Historia Clínica:

"""Esta clase simula todo el historial del paciente. Contiene una lista de turnos y una lista de recetas, 
se pueden agregar nuevos turnos o recetas, obtener las listas completas, y mostrar toda la historia clínica"""

#Clase Clínica:

"""Esta clase es la clase principal del sistema, aquella que gestiona toda la información clínica; pacientes, médicos, recetas, turnos. 
Con ella podemos agregar pacientes y medicos, podemos agendar turnos, obtener la historia clinica del paciente, emitir recetas"""

#Excepciones:

"""Utilizamos las excepciones para errores especificos que pueden surgir durante la gestion del sistema, 
por ejemplo que haya un turno duplicado, que el médico no exista o esté duplpicado, que el paciente no exista o esté duplicado y demas"""

#CLI(Command Line Interface):

"""Esta clase permite al usuario interactuar con el sistema a traves de una interfaz que proporciona un menu de opciones"""

#Tests:

"""Utilizados para verificar si el sistema está funcionando correctamente"""