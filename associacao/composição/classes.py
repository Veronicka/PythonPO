"""Uma classe é dona de classes de outra classe, ou seja, 
se uma classe é apagada a outra consequentemente é também

A classe Endereco compoe a classe Cliente (ela pertence ao cliente)
assim q um cliente é apagado, seus endereços também são apagados
"""

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
    
    def __del__(self):
        print(f"{self.nome} foi apagado")


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    
    def __del__(self):
        print(f"{self.cidade}/{self.estado} foi apagado")
