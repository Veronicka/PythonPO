# para a criação de aluno e cliente, não precisamos replicar o codigo pois ambos são pessoas
# Logo cliente e aluno herdaram pessoa e Cliente e Aluno são subclasses da super classe Pessoa

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeclasse} falando ...')

class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nomeclasse} comprando ...")

class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nomeclasse} estudando ...")
