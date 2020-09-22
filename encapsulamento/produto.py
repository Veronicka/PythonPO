class Produto:    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.upper()

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        self._preco = valor


p1 = Produto('Camiseta', 50)
p2 = Produto('Caneca', 20)
p3 = Produto('Chinelo', "R$15")

p1.desconto(20)
p2.desconto(5)
p3.desconto(10)
print(p1.nome, p1.preco)
print(p2.preco)
print(p3.preco)