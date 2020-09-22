""" Associação é associar comportamentos entre classes"""

from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Veronica')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever(escritor.nome)


