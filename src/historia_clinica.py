from datetime import datetime
from typing import List 
from src.paciente import Paciente
from src.turno import Turno
from src.receta import Receta

class HistClinica:
    def __init__(self, paciente: Paciente, turnos: List[Turno], recetas: List[Receta]):
        self.__paciente__ = paciente
        self.__turnos__ = turnos
        self.__recetas__ = recetas
    
    def agregar_turno(self, turno: Turno):
        self.__turnos__.append(turno) 
    
    def obtener_turnos(self) -> List[Turno]:
        return self.__turnos__
   
    def obtener_recetas(self) -> List[Receta]:
        return self.__recetas__
   
    def agregar_receta(self, receta: Receta):
        self.__recetas__.append(receta)
   
    def __str__(self):
        partes = [f"Historia Clínica de {self.__paciente__}"]

        if self.__turnos__:
            partes.append("Turnos:")
            partes.extend(str(t) for t in self.__turnos__)
        else:
            partes.append("Sin turnos registrados")

        if self.__recetas__:
            partes.append("Recetas:")
            partes.extend(str(r) for r in self.__recetas__)
        else:
            partes.append("Sin recetas registradas")

        return "\n".join(partes)
