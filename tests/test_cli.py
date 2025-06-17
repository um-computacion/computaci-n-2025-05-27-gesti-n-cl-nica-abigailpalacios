import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src.cli import CLI
from src.excepciones import PacienteExistente, MedicoExistente, PacienteNoExiste, MedicoNoExiste, TurnoDuplicado, EspecialidadNoDisponible, RecetaNoValida, FechaIncorrecta
from src.paciente import Paciente
from src.medico import Medico
from src.clinica import Clinica
from src.especialidad import Especialidad

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.cli = CLI()

###Tests Pacientes

    @patch("builtins.input", side_effect=["46547653", "Martin", "Sanchez", "20/12/2004"])
    def test_agendar_paciente_valido(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_paciente()
            mock_print.assert_called_with("Paciente Martin agendado exitosamente.")

    @patch("builtins.input", side_effect=["", "Martin", "Sanchez", "20/12/2004"])
    def test_agendar_paciente_dni_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_paciente()
            mock_print.assert_called_with("El DNI no puede estar vacío.")

    @patch("builtins.input", side_effect=["46547653", "", "Sanchez", "20/12/2004"])
    def test_agendar_paciente_nombre_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_paciente()
            mock_print.assert_called_with("El nombre no puede estar vacío.")

    @patch("builtins.input", side_effect=["46547653", "Martin", "", "20/12/2004"])
    def test_agendar_paciente_apellido_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_paciente()
            mock_print.assert_called_with("El apellido no puede estar vacío.")

    @patch("builtins.input", side_effect = ["46547653", "Martin", "Sanchez", ""])
    def test_agendar_paciente_fecha_vacia(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_paciente()
            mock_print.assert_called_with("La fecha de nacimiento no puede estar vacía.")

    @patch("builtins.input", side_effect=["46547653", "Martin", "Sanchez", "31/12/2025"])
    def test_agendar_paciente_fecha_invalida(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_paciente()
            self.assertFalse(any("formato no valido" in str(c[0][0]).lower() or "formato" in str(c[0][0]).lower() for c in mock_print.call_args_list))

    @patch("builtins.print")
    def test_ver_pacientes(self, mock_print):
        paciente = Paciente ("46547653", "Martin", "Sanchez", "20/12/2004")
        self.cli.clinica.__pacientes__ = {"46547653": paciente}
        self.cli.ver_pacientes()
        mock_print.assert_any_call(paciente)

    @patch("builtins.print")
    def test_ver_pacientes_vacio(self, mock_print):
        self.cli.clinica.__pacientes__ = {}
        self.cli.ver_pacientes()
        mock_print.assert_not_called()        

    @patch("builtins.input", side_effect = ["   46547657   ", "   Martin   ", "   Sanchez   ", "   20/12/2004   "])
    def test_agendar_paciente_con_espacios(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_paciente()
            mock_print.assert_called_with("Paciente Martin agendado exitosamente.")

###Tests Medicos

    @patch("builtins.input", side_effect = ["22901180", "Claudia", "Siragusa", "Neurologia", "M12345"])
    def test_agendar_medico_valido(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_medico()
            mock_print.assert_any_call("Medico/a agregado exitosamente.")

    @patch("builtins.input", side_effect=["", "Claudia", "Siragusa", "Neurologia", "M12345"])
    def test_agendar_medico_dni_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_medico()
            mock_print.assert_called_with("El DNI no puede estar vacío.")

    @patch("builtins.input", side_effect=["22901180", "", "Siragusa", "Neurologia", "M12345"])
    def test_agendar_medico_nombre_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_medico()
            mock_print.assert_called_with("El nombre no puede estar vacío.")

    @patch("builtins.input", side_effect=["22901180", "Claudia", "", "Neurologia", "M12345"])
    def test_agendar_medico_apellido_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_medico()
            mock_print.assert_called_with("El apellido no puede estar vacío.")

    @patch("builtins.input", side_effect=["22901180", "Claudia", "Siragusa", "", "M12345"])
    def test_agendar_medico_especialidad_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_medico()
            mock_print.assert_called_with("La especialidad no puede estar vacía.")    
            
    @patch("builtins.input", side_effect=["22901180", "Claudia", "Siragusa", "Neurologia", ""])
    def test_agendar_medico_matricula_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_medico()
            mock_print.assert_called_with("La matrícula no puede estar vacía.")            

    @patch("builtins.print")
    def test_ver_medicos(self, mock_print):
        medico = Medico("22901180", "Claudia", "Siragusa", ["Neurologia"], "M12345")
        self.cli.clinica.__medicos__ = {"22901180": medico}
        self.cli.ver_medicos()
        mock_print.assert_any_call(medico)

    @patch("builtins.print")
    def test_ver_medicos_vacio(self, mock_print):
        self.cli.clinica.__medicos__ = {}
        self.cli.ver_medicos()
        mock_print.assert_not_called()

    @patch("builtins.input", side_effect=["   22901180   ", "   Claudia   ", "   Siragusa   ", "   Neurologia   ", "   M12345   "])
    def test_agendar_medico_con_espacios(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_medico()
            mock_print.assert_any_call("Medico/a agregado exitosamente.")

###Tests Turnos


    @patch("builtins.input", side_effect=["46547653", "M12345", "Fecha Invalida", "jueves"])
    def test_agendar_turno_fecha_invalida(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_turno()
            self.assertFalse(any("formato no valido" in str(c[0][0]).lower() or "formato" in str(c[0][0]).lower() for c in mock_print.call_args_list))

    @patch("builtins.print")
    def test_turno_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.clinica.agendar_turno = MagicMock()
            self.cli.ver_turnos()
            mock_print.assert_not_called()

    @patch("builtins.input", side_effect=["46547653", "M12345", "21/07/2025 09:45", "jueves"])
    def test_agendar_turno_duplicado(self, mock_input):
        self.cli.clinica.agendar_turno = MagicMock(side_effect=TurnoDuplicado("Turno duplicado"))
        with patch("builtins.print") as mock_print:
            self.cli.agendar_turno()
            mock_print.assert_called_with("El turno ya esta agendado")

    @patch("builtins.input", side_effect=["46547653", "M12345", "21/07/2025 09:45", "jueves"])
    def test_agendar_turno_especialidad_no_disponible(self, mock_input):
        self.cli.clinica.agendar_turno = MagicMock(side_effect=EspecialidadNoDisponible("La especialidad no está disponible"))
        with patch("builtins.print") as mock_print:
            self.cli.agendar_turno()
            mock_print.assert_any_call("La especialidad no está disponible")

    @patch("builtins.input", side_effect=["46547653", "M12345", "21/07/2025 09:45", "jueves"])
    def test_agendar_turno_medico_no_valido(self, mock_input):
        self.cli.clinica.agendar_turno = MagicMock(side_effect=MedicoNoExiste("Medico no encontrado"))
        with patch("builtins.print") as mock_print:
            self.cli.agendar_turno()
            mock_print.assert_any_call("Medico no encontrado")

    @patch("builtins.print")
    def test_ver_turnos(self, mock_print):
        turno_mock = MagicMock()
        turno_mock.__str__.return_value = "Turno Mock"
        self.cli.clinica.obtener_turnos = MagicMock(return_value=[turno_mock])
        self.cli.ver_turnos()
        mock_print.assert_any_call(turno_mock)

    @patch("builtins.input", side_effect=["46547653", "M12345", "21/07/2025 09:45", "jueves"])
    def test_agendar_turno_completo(self, mock_input):
        turno_mock = MagicMock()
        self.cli.clinica.agendar_turno = MagicMock(return_value=turno_mock)
        with patch("builtins.print") as mock_print:
            self.cli.agendar_turno()
            mock_print.assert_any_call(f"Turno agendado: {turno_mock}")

    @patch("builtins.input", side_effect=["4652", "M12345", "21/07/2025 09:45", "jueves"])
    def test_agendar_paciente_inexistente(self, mock_input):
        self.cli.clinica.agendar_turno = MagicMock (side_effect = PacienteNoExiste ("Paciente no encontrado"))
        with patch("builtins.print") as mock_print:
            self.cli.agendar_turno()
            mock_print.assert_any_call("Paciente no encontrado")

    @patch("builtins.input", side_effect=["   46547653   ", "   M12345   ", "   21/07/2025 09:45   ", "   jueves   "])
    def test_agendar_turno_con_espacios(self, mock_input):
        turno_mock = MagicMock()
        self.cli.clinica.agendar_turno = MagicMock(return_value=turno_mock)
        with patch("builtins.print") as mock_print:
            self.cli.agendar_turno()
            mock_print.assert_any_call(f"Turno agendado: {turno_mock}")

    @patch("builtins.input", side_effect=["46547653", "M12345", "21/07/2025 09:45", "jueves"])
    def test_agendar_turno_dup(self, mock_input):
        self.cli.clinica.agendar_turno = MagicMock (side_effect = TurnoDuplicado("El turno ya esta agendado"))
        with patch("builtins.print") as mock_print:
            self.cli.agendar_turno()
            mock_print.assert_any_call("El turno ya esta agendado")

    @patch("builtins.input", side_effect=["46547653", "M12345", "21/07/2025 09:45", "jueves"])
    def test_agendar_turno_especialidad_no_disponible(self, mock_input):
        self.cli.clinica.agendar_turno = MagicMock(side_effect=EspecialidadNoDisponible("La especialidad no está disponible"))
        with patch("builtins.print") as mock_print:
            self.cli.agendar_turno()
            mock_print.assert_any_call("La especialidad no está disponible")

    @patch("builtins.input", side_effect=["", "M12345", "21/07/2025 09:45", "jueves"])
    def test_agendar_turno_dni_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agendar_turno()
            mock_print.assert_called_with("El DNI no puede estar vacio.")

###Test Recetas

    @patch("builtins.input", side_effect=["46547653", "M12345", "Paracetamol, Ibuprofeno"])
    def test_emitir_receta_valida(self, mock_input):
        receta_mock = MagicMock()
        self.cli.clinica.emitir_receta = MagicMock(return_value=receta_mock)
        with patch("builtins.print") as mock_print:
            self.cli.emitir_receta()
            mock_print.assert_any_call(f"Receta emitida exitosamente: {receta_mock}")

    @patch("builtins.input", side_effect=["46547653", "M12345", ""])
    def test_emitir_receta_vacia(self, mock_input):
        self.cli.clinica.emitir_receta = MagicMock(side_effect=RecetaNoValida("La receta no puede estar vacia"))
        with patch("builtins.print") as mock_print:
            self.cli.emitir_receta()
            mock_print.assert_any_call("La receta no puede estar vacia")

    @patch("builtins.input", side_effect=["4652", "M12345", "Paracetamol, Ibuprofeno"])
    def test_emitir_receta_paciente_no_existe(self, mock_input):
        self.cli.clinica.emitir_receta = MagicMock(side_effect = PacienteNoExiste ("El paciente no existe"))
        with patch("builtins.print") as mock_print:
            self.cli.emitir_receta()
            mock_print.assert_any_call("El paciente no existe")

    @patch("builtins.input", side_effect=["46547653", "M509", "Paracetamol, Ibuprofeno"])
    def test_emitir_receta_medico_no_existe(self, mock_input):
        self.cli.clinica.emitir_receta = MagicMock(side_effect = MedicoNoExiste ("El medico no existe"))
        with patch("builtins.print") as mock_print:
            self.cli.emitir_receta()
            mock_print.assert_any_call("El medico no existe")

    @patch("builtins.input", side_effect=["46547653", "M12345", "Cereza, Frutilla"])
    def test_emitir_receta_medicamentos_invalidos(self, mock_input):
        self.cli.clinica.emitir_receta = MagicMock(side_effect=ValueError("Error al procesar los medicamentos"))
        with patch("builtins.print") as mock_print:
            self.cli.emitir_receta()
            mock_print.assert_any_call("Error al procesar los medicamentos")

    @patch("builtins.input", side_effect=["   46547653   ", "   M12345   ", "   Paracetamol, Ibuprofeno   "])
    def test_emitir_receta_con_espacios(self, mock_input):
        receta_mock = MagicMock()
        self.cli.clinica.emitir_receta = MagicMock(return_value=receta_mock)
        with patch("builtins.print") as mock_print:
            self.cli.emitir_receta()
            mock_print.assert_any_call(f"Receta emitida exitosamente: {receta_mock}")

    @patch("builtins.input", side_effect = ["46547653", "M12345", "Paracetamol, ,Ibuprofeno, ,Tranquinal"])
    def test_emitir_receta_espacios_intermedios(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.clinica.emitir_receta = MagicMock()
            self.cli.emitir_receta()
            self.cli.clinica.emitir_receta.assert_called_with("46547653", "M12345", ["Paracetamol", "Ibuprofeno", "Tranquinal"])

    @patch("builtins.input", side_effect=["", "M12345", "Paracetamol, Ibuprofeno"])
    def test_emitir_receta_dni_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.emitir_receta()
            mock_print.assert_any_call("El DNI no puede estar vacío.")

###Test Especialidad

    @patch("builtins.input", side_effect=["M12345", "Neurologia", "jueves", "."])
    def test_agregar_especialidad_valida(self, mock_input):
        medico_mock = MagicMock()
        self.cli.clinica.obtener_medico_por_matricula = MagicMock(return_value=medico_mock)
        with patch("builtins.print") as mock_print:
            self.cli.agregar_especialidad()
            mock_print.assert_called_with("Especialidad agregada exitosamente")

    @patch("builtins.input", side_effect=["M12345", "", "jueves", "."])
    def test_agregar_especialidad_nombre_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agregar_especialidad()
            mock_print.assert_called_with("La especialidad no puede estar vacía.")

    @patch("builtins.input", side_effect=["", "Neurologia", "jueves", "."])
    def test_agregar_especialidad_matricula_vacia(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.agregar_especialidad()
            mock_print.assert_called_with("La matrícula no puede estar vacía.")

    @patch("builtins.input", side_effect=["M630", "Neurologia", "jueves", "."])
    def test_agregar_especialidad_medico_no_encontrado(self, mock_input):
        self.cli.clinica.obtener_medico_por_matricula = MagicMock(side_effect=MedicoNoExiste("Medico no encontrado"))
        with patch("builtins.print") as mock_print:
            self.cli.agregar_especialidad()
            mock_print.assert_called_with("El médico no existe")

    @patch("builtins.input", side_effect=["M12345", "Neurologia", "comingo", "."])
    def test_agregar_especialidad_dia_invalido(self, mock_input):
        self.cli.clinica.obtener_medico_por_matricula = MagicMock(return_value=MagicMock())
        with patch("builtins.print") as mock_print:
            self.cli.agregar_especialidad()
            self.assertTrue(any("inválido" in str(c[0][0]).lower() for c in mock_print.call_args_list))

    @patch("builtins.input", side_effect=["M12345", "Neurologia", "jueves", "."])
    def test_agregar_especialidad(self, mock_input):
        medico_mock = MagicMock()
        self.cli.clinica.obtener_medico_por_matricula = MagicMock(return_value=medico_mock)
        with patch("builtins.print") as mock_print:
            self.cli.agregar_especialidad()
            medico_mock.agregar_especialidad.assert_called_once()
            mock_print.assert_called_with("Especialidad agregada exitosamente")

    @patch("builtins.input", side_effect=["M12345", "Neurologia", "jueves", "."])
    def test_agregar_especialidad_error_medico(self, mock_input):
        medico_mock = MagicMock()
        self.cli.clinica.obtener_medico_por_matricula = MagicMock(return_value=medico_mock)
        medico_mock.agregar_especialidad.side_effect = ValueError("Error al agregar especialidad")
        with patch("builtins.print") as mock_print:
            self.cli.agregar_especialidad()
            mock_print.assert_any_call("Error al procesar los días de la semana: Error al agregar especialidad")

    @patch("builtins.input", side_effect=["   M12345   ", "    Neurologia   ", "   jueves   ", "."])
    def test_agregar_especialidad_con_espacios_extras(self, mock_input):
        medico_mock = MagicMock()
        self.cli.clinica.obtener_medico_por_matricula = MagicMock(return_value=medico_mock)
        with patch("builtins.print") as mock_print:
            self.cli.agregar_especialidad()
            mock_print.assert_called_with("Especialidad agregada exitosamente")

###Test Historia Clinica

    @patch("builtins.input", side_effect = ["46547653"])
    def test_ver_historia_clinica_valida(self, mock_input):
        historia_mock = "Historia Clinica del Paciente"
        self.cli.clinica.obtener_historia_clinica_por_dni = MagicMock(return_value=historia_mock)
        with patch("builtins.print") as mock_print:
            self.cli.ver_historia_clinica()
            mock_print.assert_any_call(historia_mock)

    @patch("builtins.input", side_effect = [""])
    def test_ver_historia_clinica_dni_vacio(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.cli.ver_historia_clinica()
            mock_print.assert_called_with("El DNI no puede estar vacío.")

    @patch("builtins.input", side_effect = ["0000"])
    def test_ver_historia_clinica_paciente_no_existe(self, mock_input):
        self.cli.clinica.obtener_historia_clinica_por_dni = MagicMock(side_effect=PacienteNoExiste("El paciente no existe"))
        with patch("builtins.print") as mock_print:
            self.cli.ver_historia_clinica()
            mock_print.assert_called_with("El paciente no existe")

    @patch("builtins.input", side_effect = ["   46547653   "])
    def test_ver_historia_clinica_con_espacios(self, mock_input):
        historia_mock = "Historia Clinica del Paciente"
        self.cli.clinica.obtener_historia_clinica_por_dni = MagicMock(return_value=historia_mock)
        with patch("builtins.print") as mock_print:
            self.cli.ver_historia_clinica()
            mock_print.assert_any_call(historia_mock)


if __name__ == "__main__":
    unittest.main()