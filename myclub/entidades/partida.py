from datetime import date

class Partida:
    def __init__(self, local, data, dia, mes, ano, gols_mandante, gols_adversario, mandante, adversario, presentes, presentes_tela):
        self.__local = local
        self.__data_comparacao = date(int(ano), int(mes), int(dia))
        self.__data = data
        self.__gols_adversario = gols_adversario
        self.__gols_mandante = gols_mandante
        self.__mandante = mandante
        self.__adversario = adversario
        self.__presentes = presentes
        self.__presentes_tela = presentes_tela
        self.__lista_gols = []
        self.__lista_cartoes_amarelos = []
        self.__lista_cartoes_vermelhos = []
    
    @property
    def local(self):
        return self.__local

    @property
    def data(self):
        return self.__data

    @property
    def data_comparacao(self):
        return self.__data_comparacao

    @property
    def gols_mandante(self):
        return self.__gols_mandante

    @property
    def gols_adversario(self):
        return self.__gols_adversario

    @property
    def horario(self):
        return self.__horario

    @property
    def mandante(self):
        return self.__mandante

    @property
    def adversario(self):
        return self.__adversario

    @property
    def presentes(self):
        return self.__presentes

    @property
    def presentes_tela(self):
        return self.__presentes_tela

    @property
    def lista_gols(self):
        return self.__lista_gols

    @property
    def lista_cartoes_amarelos(self):
        return self.__lista_cartoes_amarelos

    @property
    def lista_cartoes_vermelhos(self):
        return self.__lista_cartoes_vermelhos
    
    def listar_gols(self):
        for presente in self.presentes:
            if presente.gols > 0:
                self.lista_gols.append(str(presente.nome) + str('(') + str(presente.gols) + str(')'))

    def listar_cartoes_amarelos(self):
        for presente in self.presentes:
            if presente.cartoes_amarelos > 0:
                self.lista_cartoes_amarelos.append(str(presente.nome) + str('(') + str(presente.cartoes_amarelos) + str(')'))

    def listar_cartoes_vermelhos(self):
        for presente in self.presentes:
            if presente.cartoes_vermelhos > 0:
                self.lista_cartoes_vermelhos.append(str(presente.nome) + str('(') + str(presente.cartoes_vermelhos) + str(')'))