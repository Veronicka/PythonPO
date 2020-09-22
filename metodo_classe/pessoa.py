from random import randint

class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        return randint(10000, 19999)

    
p1 = Pessoa('Veronica', 26)
print(p1.get_ano_nascimento())
print(p1.gera_id())
p2 = Pessoa.por_ano_nascimento('Veronica', 1994)
print(p2.idade)
print(Pessoa.gera_id())