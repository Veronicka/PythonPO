class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, valor):
        self.__ferramenta = valor

class Caneta:
    def __init__(self, marca):
        self.__marca = marca
    
    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print(f'Caneta {self.marca} está escrevendo ...')
    
class MaquinaDeEscrever():
    def escrever(self, nome):
        print(f"{nome} está usando a maquina de escrever ...")
           