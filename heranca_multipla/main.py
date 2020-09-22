"""Herança Multipla - Quando uma classe herda de mais de uma outra classe. 
Geralmente usada em classes 'Mixin', que nada mais é que uma classe abstrada, 
que não foi feita para ser instanciada diretamente, ela terá uma funcionalidade para adicionar em outra classe. 
Essa classe Mixin, não está presenta na hierarquia de classes

Problema do diamante -  quando uma classe com herança multipla herda um mesmo método de duas classes. 
Em python em herança, o codigo busca da direita para a esquerda, se ele encontrar no primeiro ele retorna"""

from smartphone import Smartphone

smartphone = Smartphone('Pocophone F1')
smartphone.conetar()
smartphone.desligar()
smartphone.ligar()
smartphone.conetar()
smartphone.conetar()
smartphone.conetar()
smartphone.desligar()
smartphone.conetar()
smartphone.desconectar()
smartphone.desconectar()
