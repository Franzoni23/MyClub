import datetime
from myclub.entidades.partida import Partida

class Jogador:
    def __init__(self, nome, numero, nascimento, posicao):
        self.__nome = nome
        self.__numero = numero
        self.__nascimento = nascimento
        self.__idade = None
        self.__posicao = posicao
        self.__gols = '000'
        self.__cartoes_amarelos = '000'
        self.__cartoes_vermelhos = '000'
        self.__partidas = []

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
    def partidas(self):
        return self.__partidas
    
    @property
    def posicao(self):
        return self.__posicao

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
    def qtd_partidas(self):
        qtd = 00
        for partida in self.partidas:
            qtd = qtd + 1
        if qtd < 100:
            qtd = '00' + str(qtd)
        return qtd

    def atualiza_gols(self):
        gols_lista = []
        for partida in self.partidas:
            for presente in partida.presentes:
                if presente.nome == self.nome:
                    gols_lista.append(presente.gols)
        gols = sum(gols_lista)
        if gols < 10:
            gols = '00' + str(gols)
        elif gols >= 10 and gols < 100:
            gols = '0' + str(gols)
        else:
            gols = str(gols)
        self.__gols = gols

    def atualiza_cartoes_amarelos(self):
        cartoes_lista = []
        for partida in self.partidas:
            for presente in partida.presentes:
                if presente.nome == self.nome:
                    cartoes_lista.append(presente.cartoes_amarelos)
        cartoes_amarelos = sum(cartoes_lista)
        if cartoes_amarelos < 10:
            cartoes_amarelos = '00' + str(cartoes_amarelos)
        elif cartoes_amarelos >= 10 and cartoes_amarelos < 100:
            cartoes_amarelos = '0' + str(cartoes_amarelos)
        else:
            cartoes_amarelos = str(cartoes_amarelos)
        self.__cartoes_amarelos = cartoes_amarelos

    def atualiza_cartoes_vermelhos(self):
        cartoes_lista = []
        for partida in self.partidas:
            for presente in partida.presentes:
                if presente.nome == self.nome:
                    cartoes_lista.append(presente.cartoes_vermelhos)
        cartoes_vermelhos = sum(cartoes_lista)
        if cartoes_vermelhos < 10:
            cartoes_vermelhos = '00' + str(cartoes_vermelhos)
        elif cartoes_vermelhos >= 10 and cartoes_vermelhos < 100:
            cartoes_vermelhos = '0' + str(cartoes_vermelhos)
        else: 
            cartoes_vermelhos = str(cartoes_vermelhos)
        self.__cartoes_vermelhos = cartoes_vermelhos
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @numero.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @nascimento.setter
    def nascimento(self, nova_data):
        self.__nascimento = nova_data

    @posicao.setter
    def posicao(self, nova_posicao):
        self.__posicao = nova_posicao

    @cartoes_amarelos.setter
    def cartoes_amarelos(self, cartoes_amarelos):
        self.__cartoes_amarelos = cartoes_amarelos
    
    @cartoes_vermelhos.setter
    def cartoes_vermelhos(self, cartoes_vermelhos):
        self.__cartoes_vermelhos = cartoes_vermelhos

    @gols.setter
    def gols(self, gols):
        self.__gols = gols