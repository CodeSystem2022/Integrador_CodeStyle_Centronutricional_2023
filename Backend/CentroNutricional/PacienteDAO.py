from paciente import Paciente
from Conexion import Conexion
from logger_base import log

class PacienteDAO:

    _SELECT = "SELECT * FROM paciente ORDER BY id_paciente"
    _INSERT = "INSERT INTO paciente(nombre, apellido, peso, altura, imc" \
            "VALUES (%s, %s, %s, %s, %s) RETURNING id_paciente"
    _UPDATE = "UPDATE paciente SET nombre= %s, apellido=%s, peso=%s, altura=%s WHERE id_paciente=%s RETURNING id_paciente"
    _DELETE = "DELETE FROM paciente WHERE id_paciente=%s"

    _SELECT_PACIENTE = "SELECT * FROM paciente WHERE id_paciente=%s"
    _SELECT_PACIENTES_ELIMINADOS= "SELECT * FROM pacientes_eliminados"
    