import datetime
from myclub.entidades.partida import Partida

class Jogador:
    def __init__(self, nome, numero, nascimento, posicao):
        self.__nome = nome
        self.__numero = numero
        self.__nascimento = nascimento
        self.__idade = None
        self.__posicao = posicao

    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @property
    def nascimento(self):
        return self.__nascimento
    
    @property
    def idade(self):
        data = datetime.datetime.now()
        idade = int(data.year) - int(self.nascimento[6:10]) - 1
        if int(data.month) > int(self.nascimento[3:5]):
            idade = idade + 1
        if int(data.month) == int(self.nascimento[:2]):
            if int(data.day) >= int(self.nascimento[:2]):
                idade = idade + 1
        self.__idade = idade
        return self.__idade
    
    @property
    def posicao(self):
        return self.__posicao

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero

    @nascimento.setter
    def nascimento(self, nova_data):
        self.__nascimento = nova_data

    @posicao.setter
    def posicao(self, nova_posicao):
        self.__posicao = nova_posicao