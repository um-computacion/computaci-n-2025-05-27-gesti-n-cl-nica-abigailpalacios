from src.excepciones import FechaIncorrecta
from datetime import datetime

class Paciente:
    def __init__(self, dni: int, nombre: str, apellido:str, fecha_nacimiento:str):
        if not dni or not nombre or not fecha_nacimiento:
            raise ValueError("Todos los campos del paciente son obligatorios")

        try:
            datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise FechaIncorrecta("Formato de fecha incorrecto. Use DD/MM/AAAA")

        self.__dni__ = dni
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__fecha_nacimiento__ = fecha_nacimiento

    def obtener_dni(self)-> str:
        return self.__dni__

    def __str__ (self) -> str:
        return f"{self.__nombre__} {self.__apellido__} ({self.__dni__}) - Fecha de Nacimiento: {self.__fecha_nacimiento__}"