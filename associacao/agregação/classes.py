"""Faz parte da Associação
Agregação são relação de toda parte, essas classes precisam da outra classe
ex abaixo, a classe Carrinho de Compras precisa da classe Produto"""

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    
    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def valor(self):
        return self.__valor