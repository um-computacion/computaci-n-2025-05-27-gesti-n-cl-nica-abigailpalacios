
from datetime import datetime
from typing import Dict, List   
from src.paciente import Paciente
from src.medico import Medico
from src.turno import Turno
from src.historia_clinica import HistClinica
from src.especialidad import Especialidad
from src.receta import Receta
from src.excepciones import PacienteNoExiste, MedicoNoExiste, TurnoDuplicado, FechaIncorrecta, PacienteExistente, MedicoExistente, EspecialidadNoDisponible, RecetaNoValida

class Clinica:
    def __init__(self, pacientes: Dict[str, Paciente], medicos: Dict[str, Medico],turnos: List[Turno], historias_clinicas: Dict[str, HistClinica]):
        self.__pacientes__ = pacientes 
        self.__medicos__ = medicos 
        self.__turnos__ = turnos
        self.__historia_clinica__ = historias_clinicas
    
#Acceso a informacion

    def agregar_paciente(self, __paciente__: Paciente):
        dni = str(__paciente__.obtener_dni())
        if dni in self.__pacientes__:
            raise PacienteExistente("El paciente ingresado ya existe.")
        self.__pacientes__[dni] = __paciente__
        self.__historia_clinica__[dni] = HistClinica(__paciente__, [], [])

    def agregar_medico(self, __medico__: Medico):
        matricula = __medico__.obtener_matricula()
        if matricula in self.__medicos__:
            raise MedicoExistente("El médico ingresado ya existe.")
        self.__medicos__[matricula] = __medico__

    def agendar_turno(self, __dni__: Paciente, __matricula__: str, __fecha_hora__: datetime, __dia_semana__: str):
        if __dni__ not in self.__pacientes__:
            raise PacienteNoExiste("El paciente no existe.")
        if __matricula__ not in self.__medicos__:
            raise MedicoNoExiste("El médico no existe.")
            
        

        medico = self.__medicos__[__matricula__]
        especialidad = medico.obtener_especialidad(__dia_semana__)
        if not especialidad:
            raise EspecialidadNoDisponible("El médico no tiene la especialidad solicitada disponible en el día indicado.")
        
        
        self.validar_turno_no_duplicado(__matricula__, __fecha_hora__, __dia_semana__)
        
        __turno__ = Turno(self.__pacientes__[__dni__], medico, __fecha_hora__, especialidad, __dia_semana__)
        self.__turnos__.append(__turno__)
        self.__historia_clinica__[__dni__].agregar_turno(__turno__)
        return __turno__

    def emitir_receta(self, __dni__: str, __matricula__: str, __medicamentos__: list[str]):
        if __dni__ not in self.__pacientes__:
            raise PacienteNoExiste("El paciente no existe.")
        if __matricula__ not in self.__medicos__:
            raise MedicoNoExiste("El médico no existe.")
        if not __medicamentos__:
            raise RecetaNoValida("La receta no puede estar vacía.")
        
        __receta__ = Receta(self.__pacientes__[__dni__], self.__medicos__[__matricula__], __medicamentos__)
        self.__historia_clinica__[__dni__].agregar_receta(__receta__)
        return __receta__

    def obtener_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes__.values())

    def obtener_medicos(self) -> list[Medico]:
        return list(self.__medicos__.values())

    def obtener_medico_por_matricula(self, __matricula__: str) -> Medico:
        if __matricula__ not in self.__medicos__:
            raise MedicoNoExiste("El médico no existe.")
        return self.__medicos__[__matricula__]

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos__

    def obtener_historia_clinica_por_dni(self, __dni__: str) -> HistClinica: 
        if __dni__ not in self.__historia_clinica__:
            raise PacienteNoExiste("El paciente no existe.")
        return self.__historia_clinica__[__dni__]  

#validacion y utilidades

    def validar_existencia_paciente(self, __dni__: str):
        if __dni__ not in self.__pacientes__:
            raise PacienteNoExiste("El paciente no existe.")
        return True

    def validar_existencia_medico(self, __matricula__: str):
        if __matricula__ not in self.__medicos__:
            raise MedicoNoExiste("El médico no existe.")
        return True

    def obtener_dia_semana(self, __fecha_hora__: datetime) -> str:
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        return dias[__fecha_hora__.weekday()]
    
    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime, dia_semana: str):
        for turno in self.__turnos__:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora and turno.verificar_dia_semana(dia_semana):
                raise TurnoDuplicado("El turno ya está ocupado para ese médico")
    
    def validar_especialidad_en_dia(self, __medico__: Medico, __especialidad_solicitada__: str, __dia_semana__: str):
        # Verificar si el médico tiene la especialidad solicitada
        especialidades_medico = __medico__.obtener_especialidades()
        especialidad_encontrada = None
        
        for especialidad in especialidades_medico:
            if especialidad == __especialidad_solicitada__:
                especialidad_encontrada = especialidad
                break
        
        if not especialidad_encontrada:
            return False
        
        # Verificar si el médico está disponible en el día solicitado
        dias_disponibles = especialidad_encontrada.dias_disponibles
        if __dia_semana__ not in dias_disponibles:
            return False
            
        return True