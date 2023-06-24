from PacienteDAO import PacienteDAO
from Paciente import Paciente
from logger_base import log

print("**************************************************************** BIENVENIDOS A NUTRICION DIGITAL ****************************************************************");
opcion = None
while opcion != 7:
    print('****Menú principal**** ')
    print('1. Ingresar un nuevo paciente ')
    print('2. Editar paciente')
    print('3. Eliminar paciente')
    print('4. Buscar paciente')
    print('5. Listado de pacientes')
    print('6. Listado de pacienes eliminados')
    print('7. Salir')
    opcion = int(input('Digite una opción de menú(1-7): '))

    if opcion == 1:
        try:
            print('****Ingreso datos del nuevo Paciente**** ')
            nombre_paciente = input('Digite el nombre del paciente: ')
            apellido_paciente = input('Digite el apellido del paciente: ')
            peso_paciente =  float(input('Digite el peso en kg del paciente: '))
            altura_paciente =  float(input('Digite la altura en mts del paciente: '))

            paciente = Paciente(nombre=nombre_paciente,apellido=apellido_paciente,peso=peso_paciente,altura=altura_paciente)
            paciente_insertado = PacienteDAO.insertar(paciente)
            log.debug(f'Paciente insertado: {paciente_insertado}')

        except Exception as e:
            log.error(f'Ocurrió un error: {e}')

