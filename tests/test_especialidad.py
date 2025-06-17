import unittest
from src.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):

    def test_creacion_valida(self):
        especial = Especialidad("Kinesiologia", ["martes", "miércoles"])
        self.assertEqual(especial.obtener_especialidad(), "Kinesiologia")
        self.assertTrue(especial.verificar_dia("martes"))
        self.assertIn("martes", str(especial))

    def test_datos_vacios(self):
        with self.assertRaises(ValueError):
            Especialidad("", [])

    def test_dias_vacios(self):
        with self.assertRaises(ValueError):
            Especialidad("Kinesiologia", [])
    
    def test_dia_invalido(self):
        with self.assertRaises(ValueError):
            Especialidad("Kinesiologia", ["comingo"])

    def test_dia_disponible(self):
        especial = Especialidad("Kinesiologia", ["martes", "miércoles"])
        self.assertTrue(especial.verificar_dia("miércoles"))

    def test_dia_no_disponible(self):
        especial = Especialidad("Traumatologia", ["martes"])
        self.assertFalse(especial.verificar_dia("jueves"))

    def test_especialidad_no_disponible(self):
        especial = Especialidad("Traumatologia", ["martes"])
        self.assertNotEqual(especial.obtener_especialidad(), "Kinesiologia")

    def test_str_representacion(self):
        especial = Especialidad("Cardiología", ["miércoles", "viernes"])
        resultado = str(especial)
        self.assertIn("Cardiología", resultado)
        self.assertIn("viernes", resultado)

if __name__ == '__main__':
    unittest.main()