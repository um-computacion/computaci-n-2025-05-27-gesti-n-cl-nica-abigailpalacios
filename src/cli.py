from datetime import datetime
from src.clinica import Clinica
from src.paciente import Paciente
from src.medico import Medico   
from src.especialidad import Especialidad
from src.excepciones import *
from src.turno import Turno
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))


class CLI:
    def __init__(self):
        self.clinica = Clinica(pacientes={}, medicos={}, turnos=[], historias_clinicas={})

    def imprimir_menu(self):
     print("\n--- Menú Clínica ---")
     print("1) Agregar paciente")
     print("2) Agregar médico")
     print("3) Agendar turno") 
     print("4) Agregar especialidad")
     print("5) Emitir receta")
     print("6) Ver historia clínica")
     print("7) Ver todos los turnos")
     print("8) Ver todos los pacientes")
     print("9) Ver todos los médicos")
     print("0) Salir")

    def mostrar_menu(self):
        while True:
            self.imprimir_menu()
            opcion = input("Seleccione una opción: ")

            try:
                match opcion:
                    case "1":
                        self.agendar_paciente()
                    case "2":   
                        self.agendar_medico()
                    case "3":
                        self.agendar_turno()
                    case "4":
                        self.agregar_especialidad()
                    case "5":
                        self.emitir_receta()
                    case "6":
                        self.ver_historia_clinica()
                    case "7":
                        self.ver_turnos()
                    case "8":
                        self.ver_pacientes()
                    case "9":
                        self.ver_medicos()
                    case "0":
                        print ("Saliendo del programa"); 
                        break
                    case _: 
                        print("Opción no válida. Intente nuevamente.")
            except Exception as e:
                print(f"Error: {e}")        

    def agendar_paciente(self):
        try: 
            dni = input ("Ingrese DNI del paciente: ").strip()
            if not dni:
                print("El DNI no puede estar vacío.")
                return
            nombre = input("Ingrese nombre del paciente: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                return
            apellido = input("Ingrese apellido del paciente: ").strip()
            if not apellido:
                print("El apellido no puede estar vacío.")
                return
            fecha = input("Ingrese fecha de nacimiento del paciente (DD/MM/AAAA): ").strip()
            if not fecha:
                print("La fecha de nacimiento no puede estar vacía.")
                return
                
            __paciente__ = Paciente(dni, nombre, apellido, fecha)
            self.clinica.agregar_paciente(__paciente__)
            print(f"Paciente {nombre} agendado exitosamente.")

        except PacienteNoExiste as e:
            print(f"El paciente ya existe: {e}")
        except (FechaIncorrecta) as e:
            print(f"Fecha invalida: {e}")   

    def agendar_medico(self):
        try:
            dni = input("Ingrese DNI del médico: ").strip()
            if not dni:
                print("El DNI no puede estar vacío.")
                return
            nombre = input("Ingrese nombre del médico: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                return
            apellido = input("Ingrese apellido del médico: ").strip()
            if not apellido:
                print("El apellido no puede estar vacío.")
                return
            especialidad = input("Ingrese especialidad del médico: ").strip()
            if not especialidad:
                print("La especialidad no puede estar vacía.")
                return
            matricula = input("Ingrese matrícula del médico: ").strip()
            if not matricula:
                print("La matrícula no puede estar vacía.")
                return
            __medico__ = Medico(dni,nombre, apellido, [especialidad], matricula)
            self.clinica.agregar_medico(__medico__)
            print("Medico/a agregado exitosamente.")
        except MedicoNoExiste as e:
            print(f"El Medico no existe: {e}")
        except MedicoExistente as e:
            print(f"El médico ya existe: {e}")

    def agregar_especialidad(self):
        try:
            matricula = input("Ingrese matrícula del médico: ").strip()
            if not matricula:
                print("La matrícula no puede estar vacía.")
                return
            especialidad = input("Ingrese especialidad a agregar: ").strip()
            if not especialidad:
                print("La especialidad no puede estar vacía.")
                return
            dias = []
            print("Ingrese los días de la semana disponibles (para terminar agregue un punto final):")
            while True:
                dia = input("Dia: ").strip().lower()
                if dia == ".":
                    break
                if dia: dias.append(dia)
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            medico.agregar_especialidad(especialidad)
            especialidad = Especialidad(especialidad, dias)
            print("Especialidad agregada exitosamente")
        
        except MedicoNoExiste as e:
            print("El médico no existe")
        except EspecialidadNoDisponible as e:
            print("La especialidad no está disponible")
        except ValueError as e:
            print(f"Error al procesar los días de la semana: {e}")    

    def agendar_turno(self):
        try:
            dni = input("Ingrese DNI del paciente: ").strip()
            if not dni:
                print("El DNI no puede estar vacio.")
                return
            matricula = input("Ingrese matricula del médico: ").strip()
            if not matricula:
                print("La matricula no puede estar vacía.")
                return
            fecha_str = input("Fecha y hora (DD/MM/AAAA HH:MM): ").strip()
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
            dia_semana = input("Ingrese dia de la semana: ")
            turno = self.clinica.agendar_turno(dni, matricula, fecha, dia_semana)
            print(f"Turno agendado: {turno}")
        
        except PacienteNoExiste:
            print("Paciente no encontrado")
        except MedicoNoExiste:
            print("Medico no encontrado")
        except ValueError:
            print("Error al procesar la fecha y hora")
        except TurnoDuplicado:
            print("El turno ya esta agendado")
        except EspecialidadNoDisponible:
            print("La especialidad no está disponible")


    def emitir_receta(self):
        try:
            dni = input("Ingrese DNI del paciente: ").strip()
            if not dni:
                print("El DNI no puede estar vacío.")
                return
            matricula = input("Ingrese matrícula del médico: ").strip()
            if not matricula:
                print("La matrícula no puede estar vacía.")
                return
            med_str = input("Ingrese medicamentos (separados por comas): ").strip().split(",")
            medicamentos = [m.strip() for m in med_str if m.strip()]
            
            receta = self.clinica.emitir_receta(dni, matricula, [med.strip() for med in medicamentos])
            print(f"Receta emitida exitosamente: {receta}")

        except PacienteNoExiste as e:
            print("El paciente no existe")
        except MedicoNoExiste as e: 
            print("El medico no existe")
        except RecetaNoValida as e:
            print("La receta no puede estar vacia")
        except ValueError as e:
            print("Error al procesar los medicamentos")

    
    def ver_historia_clinica(self):
        try:
            dni = input("Ingrese DNI del paciente: ")
            if not dni:
                print("El DNI no puede estar vacío.")
                return
            historia_clinica = self.clinica.obtener_historia_clinica_por_dni(dni)
            print(historia_clinica)
        
        except PacienteNoExiste as e:
            print("El paciente no existe")
    
    def ver_turnos(self):
        for turno in self.clinica.obtener_turnos():
            print(turno)
    
    def ver_pacientes(self):
        for paciente in self.clinica.__pacientes__.values():
            print(paciente)

    def ver_medicos(self):
        for medico in self.clinica.__medicos__.values():
            print(medico)

if __name__ == "__main__":
    cli = CLI()
    cli.mostrar_menu()
