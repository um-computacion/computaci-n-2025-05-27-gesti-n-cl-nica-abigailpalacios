import unittest
from datetime import datetime
from src.historia_clinica import HistClinica
from src.paciente import Paciente
from src.turno import Turno
from src.receta import Receta
from src.medico import Medico
from src.especialidad import Especialidad

class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("46547653", "Martin", "Sanchez", "20/12/2004")
        self.medico = Medico("22901180", "Claudia", "Siragusa", especialidad="Neurologia", matricula="M12345")
        self.especialidad = Especialidad("Neurologia", ["jueves"])
        self.historia_clinica = HistClinica(self.paciente, [], [])

    def test_historia_clinica_inicializada(self):
        self.assertEqual(self.historia_clinica.obtener_turnos(), [])
        self.assertEqual(self.historia_clinica.obtener_recetas(), [])
        text = str(self.historia_clinica)
        self.assertIn("Sin turnos", text)
        self.assertIn("Sin recetas", text)

    def test_agregar_turno(self):
        fecha_hora = datetime(2023, 5, 27, 10, 0)
        dia_semana = "jueves"
        turno = Turno(self.paciente, self.medico, fecha_hora, self.especialidad.obtener_especialidad(), dia_semana)
        self.historia_clinica.agregar_turno(turno)
        self.assertIn(turno, self.historia_clinica.obtener_turnos())

    def test_obtener_turnos(self):
        fecha_hora = datetime(2023, 5, 27, 10, 0)
        dia_semana = "jueves"
        turno = Turno(self.paciente, self.medico, fecha_hora, self.especialidad.obtener_especialidad(), dia_semana)
        self.historia_clinica.agregar_turno(turno)
        turnos = self.historia_clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0], turno)

    def test_agregar_receta(self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol", "Ibuprofeno"])
        self.historia_clinica.agregar_receta(receta)
        self.assertIn(receta, self.historia_clinica.obtener_recetas())

    def test_obtener_recetas(self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol", "Ibuprofeno"])
        self.historia_clinica.agregar_receta(receta)
        recetas = self.historia_clinica.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertEqual(recetas[0], receta)

    def test_str_historia_clinica(self):
        text = str(self.historia_clinica)
        self.assertIn("Historia Clínica de Martin Sanchez", text)
        self.assertIn("Sin turnos registrados", text)
        self.assertIn("Sin recetas registradas", text)

        fecha_hora = datetime(2023, 5, 27, 10, 0)
        dia_semana = "jueves"
        turno = Turno(self.paciente, self.medico, fecha_hora, self.especialidad.obtener_especialidad(), dia_semana)
        self.historia_clinica.agregar_turno(turno)

        receta = Receta(self.paciente, self.medico, ["Paracetamol", "Ibuprofeno"])
        self.historia_clinica.agregar_receta(receta)

        text = str(self.historia_clinica)
        self.assertIn("Turnos:", text)
        self.assertIn(str(turno), text)
        self.assertIn("Recetas:", text)
        self.assertIn(str(receta), text)

if __name__ == '__main__':
    unittest.main()