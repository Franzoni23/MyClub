class Presente:
    def __init__(self, nome, numero, gols, cartoes_amarelos, cartoes_vermelhos):
        self.__nome = nome
        self.__numero = numero
        self.__cartoes_amarelos = cartoes_amarelos
        self.__cartoes_vermelhos = cartoes_vermelhos
        self.__gols = gols

    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @property
    def gols(self):
        return self.__gols

    @property
    def cartoes_amarelos(self):
        return self.__cartoes_amarelos

    @property
    def cartoes_vermelhos(self):
        return self.__cartoes_vermelhos

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero
