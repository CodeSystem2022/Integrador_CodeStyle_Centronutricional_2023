from PacienteDAO import PacienteDAO
from Paciente import Paciente
from logger_base import log

print(
    "**************************************************************** BIENVENIDOS A NUTRICION DIGITAL ****************************************************************");
opcion = None
while opcion != 7:
    print('****Menú principal**** ')
    print('1. Ingresar un nuevo paciente ')
    print('2. Editar paciente')
    print('3. Eliminar paciente')
    print('4. Buscar paciente')
    print('5. Listado de pacientes')
    print('6. Listado de pacientes eliminados')
    print('7. Salir')
    opcion = int(input('Digite una opción de menú(1-7): '))

    if opcion == 1:
        try:
            print('****Ingreso datos del nuevo Paciente**** ')
            nombre_paciente = input('Digite el nombre del paciente: ')
            apellido_paciente = input('Digite el apellido del paciente: ')
            peso_paciente = float(input('Digite el peso en kg del paciente: '))
            altura_paciente = float(input('Digite la altura en mts del paciente: '))

            paciente = Paciente(nombre=nombre_paciente, apellido=apellido_paciente, peso=peso_paciente,
                                altura=altura_paciente)
            paciente_insertado = PacienteDAO.insertar(paciente)
            log.debug(f'Paciente insertado: {paciente_insertado}')

        except Exception as e:
            log.error(f'Ocurrió un error: {e}')

    elif opcion == 2:
        print('****Editar paciente**** ')
        try:
            id_paciente = int(input('Digite el id del paciente a editar: '))
            nombre_paciente = input('Digite el nombre del paciente: ')
            apellido_paciente = input('Digite el apellido del paciente: ')
            peso_paciente = float(input('Digite el peso en kg del paciente: '))
            altura_paciente = float(input('Digite la altura en mts del paciente: '))
            paciente = Paciente(nombre=nombre_paciente, apellido=apellido_paciente, peso=peso_paciente,
                                altura=altura_paciente)
            paciente_actualizado = PacienteDAO.actualizar(paciente, id_paciente)
            log.debug(f'Paciente actualizado: {paciente_actualizado}')

        except Exception as e:
            log.error(f'Ocurrió un error: {e}')

    elif opcion == 3:
        print('****Eliminar paciente**** ')
        try:
            id_paciente = int(input('Digite el id del paciente a eliminar: '))
            paciente_eliminado = PacienteDAO.eliminar(id_paciente)
            log.debug('Paciente eliminado')

        except Exception as e:
            log.error(f'Ocurrió un error: {e}')

    elif opcion == 4:
        print('****Buscar paciente****')
        try:
            id_paciente = int(input('Digite el id del paciente a buscar: '))
            paciente_buscado = PacienteDAO.seleccionarPaciente(id_paciente)
            log.debug(f'Paciente encontrado: {paciente_buscado}')

        except Exception as e:
            log.error(f'Ocurrió un error: {e}')

    elif opcion == 5:
        print('****Listado de paciente****')
        try:
            pacientes = PacienteDAO.seleccionar()
            for paciente in pacientes:
                log.debug(paciente)

        except Exception as e:
            log.error(f'Ocurrió un error: {e}')

    elif opcion == 6:
        try:
            print('****Historial pacientes eliminados****')
            pacientes = PacienteDAO.pacientes_eliminados()
            for paciente in pacientes:
                log.debug(paciente)

        except Exception as e:
            log.error(f'Ocurrió un error: {e}')

    elif opcion == 7:
        print("Muchas gracias por visitar nutrición digital, lo esperamos nuevamente")
        print("******* Team Developers CodeStyle *******")
        developers = ['Dana Angellotti', 'Florencia Oviedo', 'Juan Pablo Ayoroa', 'Adriana Da Silva', 'Fernando Rojas',
                      'Ivana Germir', 'Gabriela Silva', 'Martin Verstraeten']

        for developer in developers:
            print(developer)
        break

    else:
        print("La opción es incorrecta, digite nuevamente")
