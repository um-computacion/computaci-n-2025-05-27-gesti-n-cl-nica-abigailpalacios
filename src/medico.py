from src.especialidad import Especialidad
from src.excepciones import EspecialidadNoDisponible

class Medico:
    def __init__(self, dni: int, nombre: str, apellido: str, especialidad: list[Especialidad], matricula: str):
        if not matricula or not nombre or not apellido or not dni or not especialidad:
            raise ValueError("Los campos de matrícula, dni, nombre, apellido y especialidad no pueden quedar vacíos")
    
        self.__dni__ = dni
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__matricula__ = matricula
        self.__especialidad__ = especialidad

    def obtener_matricula(self) -> str:
        return self.__matricula__
    
    
    def obtener_especialidad(self,dia: str):
        for esp in self.__especialidad__:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None
    
    def agregar_especialidad(self, especialidad):
        if not isinstance(especialidad, Especialidad):
            raise TypeError("Debe agregar una instancia de Especialidad")
        
        if isinstance(self.__especialidad__, str):
            self.__especialidad__ = []
    
        if especialidad not in self.__especialidad__: 
            self.__especialidad__.append(especialidad)

    
    def __str__ (self) -> str:
        return f"{self.__nombre__} {self.__apellido__} ({self.__dni__}) - Especialidad: {self.__especialidad__} - Matrícula: {self.__matricula__}"
    
    def obtener_especialidades(self) -> list[Especialidad]:
     return self.__especialidad__
    