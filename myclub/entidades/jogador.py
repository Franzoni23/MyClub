import datetime
from myclub.entidades.partida import Partida

class Jogador:
    def __init__(self, nome, numero, nascimento, posicao):
        self.__nome = nome
        self.__numero = numero
        self.__nascimento = nascimento
        self.__idade = None
        self.__posicao = posicao
        self.__gols = None
        self.__cartoes_amarelos = None
        self.__cartoes_vermelhos = None

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
    def gols(self):
        return self.__gols

    @property
    def cartoes_amarelos(self):
        return self.__cartoes_amarelos

    @property
    def cartoes_vermelhos(self):
        return self.__cartoes_vermelhos
    
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

    @gols.setter
    def gols(self, gols):
        self.__gols = gols

    @cartoes_amarelos.setter
    def cartoes_amarelos(self, cartoes_amarelos):
        self.__cartoes_amarelos = cartoes_amarelos

    @cartoes_vermelhos.setter
    def cartoes_vermelhos(self, cartoes_vermelhos):
        self.__cartoes_vermelhos = cartoes_vermelhos