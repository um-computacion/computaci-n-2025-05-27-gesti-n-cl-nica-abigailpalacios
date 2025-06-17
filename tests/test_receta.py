import unittest
from src.paciente import Paciente
from src.medico import Medico
from src.receta import Receta

class TestReceta(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("46547653", "Martin", "Sanchez", "20/12/2004")
        self.medico = Medico("22901180", "Claudia", "Siragusa", "Neurologia", "M12345")


    def test_receta (self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol", "Ibuprofeno"])
        self.assertIn("Paracetamol", str(receta))
        self.assertIn("Ibuprofeno", str(receta))

    def test_medicamento_invalido (self):
        with self.assertRaises (ValueError):
            Receta(self.paciente, self.medico, ["", "", ""])
        
    def test_medicamento_vacio(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, []) 

    def test_paciente_invalido(self):
        with self.assertRaises (TypeError):
            Receta("00000000", self.medico, ["Paracetamol", "Ibuprofeno"])   

    def test_medico_invalido(self):
        with self.assertRaises (TypeError):
            Receta(self.paciente, "M00000", ["Paracetamol", "Ibuprofeno"])  


if __name__ == '__main__':
    unittest.main()