class Paciente:
    def __init__(self, nombre=None,apellido=None, peso=None,altura=None):
        self._id_paciente = None
        self._nombre = nombre
        self._apellido = apellido
        self._peso = peso
        self._altura = altura
        self._imc = Paciente.calcularIMC(peso,altura)
        
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
    
    @property
    def id_paciente(self):
        return self._id_paciente
    
    id_paciente.setter
    def id_paciente(self, id_paciente):
        self._id_paciente = id_paciente
    
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, peso):
        self._peso = peso
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        self._altura = altura
    
    
    #calculamos el IMC(indice de masa corporal) a traves de un classmethod y un getter
    @classmethod
    
    def calcularIMC(cls, peso, altura):
        imc = round(peso/(altura*altura),2)# con round hacemos un redondeo a dos decimales
        return imc
    
    @property
    def imc(self):
        return self._imc
        