import unittest
from datetime import datetime
from src.paciente import Paciente
from src.excepciones import FechaIncorrecta

class TestPaciente(unittest.TestCase):

    def test_crear_paciente(self):
        paciente = Paciente("46547653", "Martin", "Sanchez", "20/12/2004")
        self.assertEqual(paciente.obtener_dni(), "46547653")
        self.assertIn("46547653", str(paciente))

    def test_fecha_invalida(self):
        with self.assertRaises(FechaIncorrecta):
            Paciente("46547653", "Martin", "Sanchez", "2027/03/07")

    def test_campos_vacios (self):
        with self.assertRaises(ValueError):
            Paciente("", "", "", "")

    def test_str_representacio(self):
        paciente = Paciente("46547653", "Martin", "Sanchez", "20/12/2004")
        igual= str(paciente)
        self.assertIn("46547653", igual)
        self.assertIn("Martin", igual)
        self.assertIn("Sanchez", igual)
        

if __name__ == '__main__':
    unittest.main()