import unittest
from datetime import datetime
from src.paciente import Paciente
from src.medico import Medico
from src.turno import Turno

class TestTurno(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente ("46547653", "Martun", "Sanchez", "20/12/2004")
        self.medico = Medico("22901180", "Claudia", "Santoni", "Neurologia", "M12345")
        self.fecha = datetime(2025,6,19,15,45)
        self.dia_semana = "jueves"

    def test_agendar_turno_valido (self):
        turno = Turno(self.paciente, self.medico, self.fecha, "Neurologia", self.dia_semana)
        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual (turno.obtener_fecha_hora(), self.fecha)
        self.assertIn ("Neurologia", str(turno))

    def test_paciente_no_encontrado(self):
        with self.assertRaises (TypeError):
            Turno("0000", self.medico, self.fecha, "Neurologia", self.dia_semana)

    def test_medico_no_encontrado(self):
        with self.assertRaises (TypeError):
            Turno(self.paciente, "M0000", self.fecha, "Neurologia", self.dia_semana)

    def test_fecha_invalida(self):
        with self.assertRaises (TypeError):
            Turno(self.paciente, self.medico, "2027, 6, 19, 17, 15", "Neurologia", self.dia_semana)

    def test_especialidad_no_encontrado(self):
        with self.assertRaises (ValueError):
            Turno(self.paciente, self.medico, self.fecha, "", self.dia_semana)


if __name__ == '__main__':
    unittest.main()