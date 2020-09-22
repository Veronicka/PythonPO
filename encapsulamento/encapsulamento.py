"""
Modificadores de acesso:
public: metodos e atributos que tem acesso dentro e fora da classe
protected: metodos e atributos que tem acesso apenas dentro da classe e por suas filhas (pacote)
private: metodos e atributos que somente a classe tem acesso

_ underline antes do atributo, esse atributo é protected
__ 2 underlines antes do atributo, esse atributo é privado
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    @property
    def dados(self):
        return self.__dados
    
    def inserir_client(self, id, nome):
        if 'clients' not in self.__dados:
            self.__dados['clients'] = { id: nome }
        else:
            self.__dados['clients'].update({ id: nome })
    
    def lista_clients(self):
        for id, nome in self.__dados['clients'].items():
            print(id, nome)

    def apaga_client(self, id):
        del self.__dados['clients'][id]


bd = BaseDeDados()
bd.inserir_client(1, 'Veronica')
bd.inserir_client(2, 'Danilo')
bd.inserir_client(3, 'Belinha')
bd.__dados = 'outra coisa'
print(bd.__dados) #aqui o python criou outro atributo, sem interferiri no privado da classe
print(bd._BaseDeDados__dados) #aqui é o atributo original da classe

print(bd.dados) #utilizar o get para ver o atributo privado é a melhor maneira, para alterar precisa criar um setter
bd.lista_clients()

