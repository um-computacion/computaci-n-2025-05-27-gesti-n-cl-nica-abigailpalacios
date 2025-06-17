from typing import List, Dict

class Especialidad:
    def __init__(self, tipo:str, dias:List[str]):
        if not tipo or not dias:
            raise ValueError("La especialidad y los días de atención son obligatorios")

        dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        for dia in dias:
            if dia.lower() not in dias_validos:
                raise ValueError(f"Día inválido: {dia}")

        self.__tipo__ = tipo
        self.__dias__ = dias
    def obtener_especialidad(self) -> str:
        return self.__tipo__

    def verificar_dia(self, dia: str) -> bool:
        return dia in self.__dias__     
    def __str__(self) -> str:
        return f"Especialidad: {self.__tipo__} - Días de atención: {self.__dias__}"