import unittest
from datetime import datetime
from src.clinica import Clinica
from src.paciente import Paciente
from src.cli import CLI
from src.medico import Medico
from src.especialidad import Especialidad
from src.excepciones import PacienteNoExiste, MedicoNoExiste, TurnoDuplicado, PacienteExistente, MedicoExistente, EspecialidadNoDisponible, RecetaNoValida
from src.receta import Receta 
from src.turno import Turno

class TestClinica(unittest.TestCase):

    def setUp(self):
        self.especialidad = Especialidad("Neurologia", ["jueves"],) 
        self.paciente = Paciente("46547653", "Martin", "Sanchez", "20/12/2004")
        self.medico = Medico("22901180", "Claudia", "Siragusa", matricula="M12345", especialidad=[self.especialidad])
        self.clinica = Clinica({}, {}, [], {})

    def test_agregar_paciente(self):
        self.clinica.agregar_paciente(self.paciente)
        self.assertIn(self.paciente, self.clinica.obtener_pacientes())

    def test_agregar_paciente_existente(self):
        self.clinica.agregar_paciente(self.paciente)
        with self.assertRaises(PacienteExistente):
            self.clinica.agregar_paciente(self.paciente)

    def test_agregar_medico(self):
        self.clinica.agregar_medico(self.medico)
        self.assertIn(self.medico, self.clinica.obtener_medicos())

    def test_agregar_medico_duplicado(self):
        self.clinica.agregar_medico(self.medico)
        with self.assertRaises(MedicoExistente):
            self.clinica.agregar_medico(self.medico)


    def test_agendar_turno_paciente_inexistente(self):
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad)

        with self.assertRaises(PacienteNoExiste):
            self.clinica.agendar_turno("99999999", "M001", datetime.now(), "lunes")

    def test_agendar_turno_medico_inexistente(self):
        self.clinica.agregar_paciente(self.paciente)
        self.medico.agregar_especialidad(self.especialidad)

        with self.assertRaises(MedicoNoExiste):
            self.clinica.agendar_turno(self.paciente.obtener_dni(), "M999", datetime.now(), "lunes")

    def test_agendar_turno_especialidad_no_disponible(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

        with self.assertRaises(EspecialidadNoDisponible):
            self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), datetime.now(), "martes")

    def test_emitir_receta_paciente_inexistente(self):
        self.clinica.agregar_medico(self.medico)

        with self.assertRaises(PacienteNoExiste):
            self.clinica.emitir_receta("99999999", self.medico.obtener_matricula(), ["Paracetamol"])

    def test_emitir_receta_medico_inexistente(self):
        self.clinica.agregar_paciente(self.paciente)

        with self.assertRaises(MedicoNoExiste):
            self.clinica.emitir_receta(self.paciente.obtener_dni(), "M999", ["Paracetamol"])

    def test_emitir_receta_sin_medicamentos(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

        with self.assertRaises(RecetaNoValida):
            self.clinica.emitir_receta(self.paciente.obtener_dni(), self.medico.obtener_matricula(), [])

    def test_obtener_historia_clinica_por_dni(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.medico.agregar_especialidad(self.especialidad) 

        fecha = datetime(2025, 6, 19, 10, 0) 
        self.clinica.agendar_turno(self.paciente.obtener_dni(), self.medico.obtener_matricula(), fecha, "jueves")
        historia = self.clinica.obtener_historia_clinica_por_dni(self.paciente.obtener_dni())
        self.assertIsNotNone(historia)
    

    def test_obtener_historia_clinica_paciente_inexistente(self):
        with self.assertRaises(PacienteNoExiste):
            self.clinica.obtener_historia_clinica_por_dni("99999999")

    def test_emitir_receta(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

        receta = self.clinica.emitir_receta("46547653", "M12345", ["Paracetamol", "Ibuprofeno"])
        self.assertIn("Paracetamol", str(receta))

    def test_emitir_receta_invalida(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

        with self.assertRaises(RecetaNoValida):
            self.clinica.emitir_receta("46547653", "M12345", [])

    def test_obtener_paciente_vacio(self):
        self.clinica.agregar_paciente(self.paciente)
        pacientes = self.clinica.obtener_pacientes()
        self.assertEqual(len(pacientes), 1)
        self.assertEqual(pacientes[0].obtener_dni(), "46547653")

    def test_obtener_medico_vacio(self):
        self.clinica.agregar_medico(self.medico)
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(medicos), 1)
        self.assertEqual(medicos[0].obtener_matricula(), "M12345")

    def test_obtener_turnos(self):
        self.clinica.agregar_paciente(self.paciente)
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agregar_medico(self.medico)
        
        fecha = datetime(2025, 6, 19, 10, 0)
        self.assertIsInstance(fecha, datetime)  # <-- validación preventiva en test
        
        turno = self.clinica.agendar_turno("46547653", "M12345", fecha, "jueves")
        self.assertIsNotNone(turno)  # confirmo que se crea turno
        self.assertEqual(turno.obtener_fecha_hora(), fecha)


    def test_agregar_especialidad_no_modifica_clinica(self):
        self.clinica.agregar_medico(self.medico)
        especialidad = Especialidad("Odontologia", ["miércoles"])
        self.medico.agregar_especialidad(especialidad)
        self.assertEqual(len(self.clinica.obtener_medicos()), 1)

if __name__ == '__main__':
    unittest.main()