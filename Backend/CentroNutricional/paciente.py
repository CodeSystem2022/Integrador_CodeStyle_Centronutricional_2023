class Paciente:
    def __init__(self, nombre=None,apellido=None, peso=None,altura=None):
        self._id_paciente = None
        self._nombre = nombre
        self._apellido = apellido
        self._peso = peso
        self._altura = altura
        self._imc = Paciente
        
    def __str__(self):
        return f'''
        Id Paciente:{self._id_paciente}
        Nombre:{self._nombre}
        Apellido:{self._apellido}
        Peso:{self._peso}
        Altura:{self._altura}
        IMC: {self._imc}
    
    '''
    
    #setters y getters