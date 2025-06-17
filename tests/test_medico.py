import unittest
from src.medico import Medico
from src.especialidad import Especialidad
from src.excepciones import TurnoDuplicado

class TestMedico(unittest.TestCase):
    
    def test_crear_medico(self):
        medico = Medico("22901180", "Claudia", "Siragusa", "Neurologia", "M12345")
        self.assertEqual(medico.obtener_matricula(), "M12345")
        self.assertIn("Siragusa", str(medico))

    def test_crear_medico_datos_invalidos(self):
        with self.assertRaises(ValueError):
            Medico("", "Claudia", "Santoni","Neurologia", "M12345")
        with self.assertRaises(ValueError):
            Medico("22901180", "", "Santoni","Neurologia", "M12345")
        with self.assertRaises(ValueError):
            Medico("22901180", "Claudia", "","Neurologia", "M12345")
        with self.assertRaises(ValueError):
            Medico("22901180", "Claudia", "Santoni","Neurologia", "")

    def test_datos_vacios(self):
        with self.assertRaises(ValueError):
            Medico("","","", "Neurologia", "")

    def test_especialidad_dia_valido(self):
        medico = Medico("22901180", "Fabiana", "Rios","Pediatria", "M38462")
        esp = Especialidad("Pediatria", ["viernes"])
        medico.agregar_especialidad(esp)
        self.assertEqual(medico.obtener_especialidad("viernes"), "Pediatria")

    def test_especialidad_para_dia_invalido(self):
        medico = Medico("47809068", "Milagros", "Santoni","Cardiología", "M98765")
        esp = Especialidad("Cardiología", ["viernes"])
        medico.agregar_especialidad(esp)
        self.assertIsNone(medico.obtener_especialidad("miércoles"))

    def test_especialidad_invalida(self):
        medico = Medico("22901180", "Claudia", "Siragusa", "Cereza", "M12345")
        with self.assertRaises(TypeError):
            medico.agregar_especialidad("Especialidad no reconocida")

    def test_especialidad_dia_duplicado(self):
        medico = Medico("23409120", "Ana", "Melendres", "Dermatologia", "M92753")
        especial = Especialidad("Dermatologia", ["miércoles"])
        medico.agregar_especialidad(especial)
        self.assertEqual(medico.obtener_especialidad("miércoles"), "Dermatologia")
        
    def test_especialidad_dia_erroneo(self):
        medico = Medico("23409120", "Ana", "Melendres", "Dermatologia", "M92753")
        especial = Especialidad("Dermatologia", ["miércoles"])
        medico.agregar_especialidad(especial)
        self.assertIsNone(medico.obtener_especialidad("domingo"))

    def test_agregar_especialidad(self):
        especialidad_inicial = Especialidad("Cardiologia", ["martes"])
        medico = Medico("22901180", "Claudia", "Siragusa", [especialidad_inicial], "M12345")
        especial = Especialidad("Neurologia", ["lunes"])
        medico.agregar_especialidad(especial)
        especialidades = medico.obtener_especialidades()
        self.assertEqual(len(especialidades), 2)
        tipos_especialidades = [esp.obtener_especialidad() for esp in especialidades]
        self.assertIn("Neurologia", tipos_especialidades)

    def test_especialidad_duplicada (self):
        especialidad_inicial = Especialidad("Neurologia", ["martes"])
        medico = Medico("22901180", "Claudia", "Siragusa", [especialidad_inicial], "12345")
        esp = Especialidad("Cardiología", ["lunes"])
        medico.agregar_especialidad(esp)
        medico.agregar_especialidad(esp) 
        especialidades = medico.obtener_especialidades()
        tipos_especialidades = [esp.obtener_especialidad() for esp in especialidades]
        self.assertEqual(tipos_especialidades.count("Cardiología"), 1)

if __name__ == '__main__':
    unittest.main()