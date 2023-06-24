from integrador_CodeStyle_Centronutricional_2023.Backend.CentroNutricional import paciente
from paciente import Paciente
from Conexion import Conexion
from logger_base import log


class PacienteDAO:
    _SELECT = "SELECT * FROM paciente ORDER BY id_paciente"
    _INSERT = "INSERT INTO paciente(nombre, apellido, peso, altura, imc)" \
              "VALUES (%s,%s,%s,%s,%s) RETURNING id_paciente"
    _UPDATE = "UPDATE paciente SET nombre = %s, apellido=%s, peso=%s, altura=%s RETURNING"
    _DELETE = "DELETE FROM paciente WHERE id_paciente=%s"

    _SELECT_PACIENTE = "SELECT * FROM paciente WHERE id_paciente=%s"
    _SELECT_PACIENTES_ELIMINADOS = "SELECT * FROM pacientes_eliminados"

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                pacientes = []  # creamos una lista
                for registro in registros:
                    id_paciente = (registro[1], registro[2],
                                   registro[3], registro[4])  # nombre, apellido, peso, altura
                    paciente.id_paciente(id_paciente)
                    pacientes.append(paciente)
                    return pacientes

    @classmethod
    def seleccionarPaciente(cls, id_paciente):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (id_paciente,)
                cursor.execute(cls._SELECT_PACIENTE, valores)
                registro = cursor.fetchone()
                id_paciente = registro[0]  # id del paciente
                paciente = Paciente(registro[1], registro[2],
                                    registro[3], registro[4])  # nombre, apellido, peso, altura
                paciente.id_paciente(id_paciente)
                return paciente

    @classmethod
    def insertar(cls, paciente):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (paciente.nombre, paciente._apellido, paciente.peso, paciente.altura, paciente.imc)
                cursor.execute(cls._INSERT, valores)
                id_paciente = cursor.fetchone()[0]
                paciente.id_paciente(id_paciente)
                log.debug(f'Paciente insertado: {paciente}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, paciente, id_paciente):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (paciente.nombre, paciente.apellido, paciente.peso, paciente.altura, id_paciente)
                cursor.execute(cls._UPDATE, valores)
                id_paciente = cursor.fetchone()[0]
                paciente.id_paciente(id_paciente)
                log.debug(f'Paciente actualizado: {paciente}')
                return cursor.rowcount

