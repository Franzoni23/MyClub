from myclub.entidades.partida import Partida
from myclub.entidades.presente import Presente
from myclub.DAO.PartidasDAO import PartidasDAO
from myclub.limites.telaPartidas import TelaPartidas
from myclub.limites.telaPartidasJogador import TelaPartidasJogador
from myclub.limites.telaCadastraPartida import TelaCadastraPartida
from operator import attrgetter
import sys
import copy


class ControladorPartida:
    def __init__(self, sistema_geral):
        self.__sistema_geral = sistema_geral
        self.__tela = TelaPartidas()
        self.__tela_jogador = TelaPartidasJogador()
        self.__tela_cadastro = TelaCadastraPartida()
        self.__partidas = PartidasDAO()
        self.__presentes = []
        self.__presentes_tela = []
    
    @property
    def partidas(self):
        return self.__partidas

    @property
    def presentes(self):
        return self.__presentes

    @property
    def presentes_tela(self):
        return self.__presentes_tela

    def finalizar(self):
        sys.exit(0)
    
    def voltar(self):
        self.__presentes = []
        self.__presentes_tela = []
        self.opcoes()
    
    def voltar_inicio(self):
        return self.__sistema_geral.inicio()
    
    def listar_partidas(self):
        lista_print = []
        lista_partidas = []
        for partida in self.__partidas.get_all():
            lista_partidas.append(partida)
        lista = sorted(lista_partidas, key=attrgetter('data_comparacao'))
        for partida in lista: 
            data = partida.data
            mandante = partida.mandante
            adversario = partida.adversario
            gols_mandante = partida.gols_mandante
            gols_adversario = partida.gols_adversario
            gols = partida.lista_gols
            lista_print.append(str(partida.data) + " - " + str(mandante) + " " + str(gols_mandante) + ' x ' + str(gols_adversario) + " " + str(adversario) + str(' - ') + str(gols))               
        return lista_print

    def listar_partidas_jogador(self, jogador_key):
        lista_print = []
        lista_partidas = []
        for partida in self.__partidas.get_all():
            for presente in partida.presentes:
                if presente.numero == jogador_key:
                    lista_partidas.append(partida)
        lista = sorted(lista_partidas, key=attrgetter('data_comparacao'))
        for partida in lista:  
            data = partida.data
            mandante = partida.mandante
            adversario = partida.adversario
            gols_mandante = partida.gols_mandante
            gols_adversario = partida.gols_adversario
            gols = partida.lista_gols
            lista_print.append(str(partida.data) + " - " + str(mandante) + " " + str(gols_mandante) + ' x ' + str(gols_adversario) + " " + str(adversario) + str(' - ') + str(gols)) 
        return lista_print

    def listar_gols(self):
        lista_print = []
        for jogador in self.sistema_geral.controlador_principal.jogadores.get_all():
                lista_print.append(jogador.nome + jogador.gols)
        return lista_print
    
    def listar_gols_jogador(self, jogador_key):
        lista_print = []
        lista_partidas = []
        for partida in self.__partidas.get_all():
            for presente in partida.presentes:
                if presente.numero == jogador_key and presente.gols > 0:
                    lista_partidas.append(partida)  
        for partida in lista_partidas:  
            data = partida.data
            mandante = partida.mandante
            adversario = partida.adversario
            gols_mandante = partida.gols_mandante
            gols_adversario = partida.gols_adversario
            gols = partida.lista_gols
            lista_print.append(str(partida.data) + " - " + str(mandante) + " " + str(gols_mandante) + ' x ' + str(gols_adversario) + " " + str(adversario) + str(' - ') + str(gols)) 
        return lista_print

    def listar_cartoes_amarelos_jogador(self, jogador_key):
        lista_print = []
        lista_partidas = []
        for partida in self.__partidas.get_all():
            for presente in partida.presentes:
                if presente.numero == jogador_key and presente.cartoes_amarelos > 0:
                    lista_partidas.append(partida)  
        for partida in lista_partidas:  
            data = partida.data
            mandante = partida.mandante
            adversario = partida.adversario
            gols_mandante = partida.gols_mandante
            gols_adversario = partida.gols_adversario
            cartoes_amarelos = partida.lista_cartoes_amarelos
            lista_print.append(str(partida.data) + " - " + str(mandante) + " " + str(gols_mandante) + ' x ' + str(gols_adversario) + " " + str(adversario) + str(' - ') + str(cartoes_amarelos)) 
        return lista_print

    def listar_cartoes_vermelhos_jogador(self, jogador_key):
        lista_print = []
        lista_partidas = []
        for partida in self.__partidas.get_all():
            for presente in partida.presentes:
                if presente.numero == jogador_key and presente.cartoes_vermelhos > 0:
                    lista_partidas.append(partida)  
        for partida in lista_partidas:  
            data = partida.data
            mandante = partida.mandante
            adversario = partida.adversario
            gols_mandante = partida.gols_mandante
            gols_adversario = partida.gols_adversario
            cartoes_vermelhos = partida.lista_cartoes_vermelhos
            lista_print.append(str(partida.data) + " - " + str(mandante) + " " + str(gols_mandante) + ' x ' + str(gols_adversario) + " " + str(adversario) + str(' - ') + str(cartoes_vermelhos)) 
        return lista_print
    
    def qtd_partidas(self):
        qtd = 0
        for partida in self.__partidas.get_all():
            qtd += 1
        return qtd  
    
    def opcoes(self):
        partidas = self.listar_partidas()
        opcoes = {'back': self.voltar_inicio, '1': self.criar_partida, '2': self.excluir_partida, '3':self.alterar_partida, None:self.finalizar}
        button, values = self.__tela.abre_tela(partidas)
        opçao_escolhida = opcoes[button]
        if button == '1':
            opçao_escolhida = opcoes[button]('vazio', self.presentes_tela)
        if button == '2' or button == '3':
            opçao_escolhida = opcoes[button](values['partida'])
        opçao_escolhida() 

    def partidas_jogador(self, jogador_key):
        partidas = self.listar_partidas_jogador(jogador_key)
        button, values = self.__tela_jogador.abre_tela(partidas)
        if button == None:
            self.finalizar()
        if button == 'back':
            self.voltar_inicio()

    def gols_jogador(self, jogador_key):
        partidas = self.listar_gols_jogador(jogador_key)
        button, values = self.__tela_jogador.abre_tela(partidas)
        if button == None:
            self.finalizar()
        if button == 'back':
            self.voltar_inicio()

    def cartoes_amarelos_jogador(self, jogador_key):
        partidas = self.listar_cartoes_amarelos_jogador(jogador_key)
        button, values = self.__tela_jogador.abre_tela(partidas)
        if button == None:
            self.finalizar()
        if button == 'back':
            self.voltar_inicio()

    def cartoes_vermelhos_jogador(self, jogador_key):
        partidas = self.listar_cartoes_vermelhos_jogador(jogador_key)
        button, values = self.__tela_jogador.abre_tela(partidas)
        if button == None:
            self.finalizar()
        if button == 'back':
            self.voltar_inicio()

    def criar_partida(self, dados_partida, presentes_tela):
        if dados_partida == 'vazio':
            dados = {'gols_mandante': '', 'gols_adversario': '', 'adversario': '', 'data': ''}
        else:
            dados = dados_partida
        jogadores = self.__sistema_geral.controlador_principal.listar_jogadores()
        button, values = self.__tela_cadastro.abre_tela(dados, jogadores, presentes_tela)
        #Dados do imput
        local = 'Campo do Inter'
        mandante = 'Família Franzoni'
        adversario = values['1']
        gols_mandante = values['2']
        gols_adversario = values['3']
        data = values['4']
        dados_partida = {'data': data, 'gols_mandante': gols_mandante, 'gols_adversario': gols_adversario, 'adversario': adversario}
        if button == 'adiciona':
            gols = values['go']
            ca = values['ca']
            cv = values['cv']
            dados_jogador = {'go': gols, 'ca': ca, 'cv':cv}
            self.adiciona_presente(values['jogador'], dados_jogador, dados_partida)
        if button == 'retira':
            self.retira_presente(values['presente'], dados_partida)
        if button == None:
            self.finalizar()
        if button == 'back':
            self.voltar()
        #Valida data
        if data == '':
            self.__tela.popup_ok('Escolha a data.')
            dados_partida = {'data': '', 'gols_mandante': gols_mandante, 'gols_adversario': gols_adversario, 'adversario': adversario}
            self.criar_partida(dados_partida, presentes_tela)
        for partida in self.partidas.get_all():
            if partida.data == data:
                self.__tela.popup_ok('Já existe outra partida nessa data.')
                dados_partida = {'data': '', 'gols_mandante': gols_mandante, 'gols_adversario': gols_adversario, 'adversario': adversario}
                self.criar_partida(dados_partida, presentes_tela)
        #Ajeita Nome
        preposicoes = ['da', 'de', 'di', 'do', 'du', 'para']
        partes_nome = []
        for parte in adversario.split():
            if not parte in preposicoes:
                parte = parte.capitalize()
            partes_nome.append(parte)
        adversario = ' '.join(partes_nome)
        #Valida Resultado:
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        todos_int = True
        todos_int2 = True
        for gol in gols_mandante:
            if gol not in numeros:
                todos_int = False
        for gol in gols_adversario:
            if gol not in numeros:
                todos_int2 = False
        if todos_int == False or todos_int2 == False or gols_mandante == '' or gols_adversario == '':
            self.__tela_cadastro.popup_ok('Digite apenas números válidos no resultado da partida.')
            dados_partida = {'data': data, 'gols_mandante': '', 'gols_adversario': '', 'adversario': adversario}
            self.criar_partida(dados_partida, presentes_tela)
        if button == 'confirma':
            presentes = copy.copy(self.presentes)
            presentes_tela = copy.copy(self.presentes_tela)
            nova_partida = Partida(local, data, data[:2], data[3:5], data[6:10], gols_mandante, gols_adversario, mandante, adversario, presentes, presentes_tela)
            nova_partida.listar_gols()
            nova_partida.listar_cartoes_amarelos()
            nova_partida.listar_cartoes_vermelhos()
            self.partidas.add(nova_partida.data, nova_partida)
            lista_jogadores = []
            for jogador in self.__sistema_geral.controlador_principal.jogadores.get_all():
                for presente in self.presentes:
                    if presente.nome == jogador.nome:
                        lista_jogadores.append(jogador)
            for jogador in lista_jogadores:
                jogador.partidas.append(nova_partida)
                jogador.atualiza_gols()
                jogador.atualiza_cartoes_amarelos()
                jogador.atualiza_cartoes_vermelhos()
                self.__sistema_geral.controlador_principal.jogadores.remove(jogador.numero)
                self.__sistema_geral.controlador_principal.jogadores.add(jogador.numero, jogador)
        self.__tela.popup_ok('Partida regristrada com sucesso!')
        self.voltar()

    def adiciona_presente(self, jogador, dados_jogador, dados_partida):
        if jogador == []:
            self.__tela_cadastro.popup_ok('Selecione um jogador para adicionar.')
            self.criar_partida('vazio', self.presentes_tela)
        jogador_key = jogador[0][0:2]
        jogador = self.__sistema_geral.controlador_principal.jogadores.get(jogador_key)
        nome = jogador.nome
        numero = jogador.numero
        gols = (int(dados_jogador['go']))
        cartoes_amarelos = (int(dados_jogador['ca']))
        cartoes_vermelhos = (int(dados_jogador['cv']))
        jogador = Presente(nome, numero, gols, cartoes_amarelos, cartoes_vermelhos)
        qtd = 0
        presente = False
        if len(self.presentes) == 0:
            self.presentes.append(jogador)
            self.presentes_tela.append(jogador.numero + " " + jogador.nome)
        else:
            for i in self.presentes:
                if i.numero == jogador.numero:
                    presente = True
            if presente == True:
                qtd = qtd + 1
            if qtd == 0:
                self.presentes.append(jogador)
                self.presentes_tela.append(jogador.numero + " " + jogador.nome)
        self.criar_partida(dados_partida, self.presentes_tela)   
    
    def retira_presente(self, presente, dados_partida):
        if presente == []:
            self.__tela_cadastro.popup_ok('Selecione um jogador para retirar.')
            self.criar_partida(dados_partida, self.presentes_tela)
        jogador_key = presente[0][0:2]
        for jogador in self.presentes:
            if jogador.numero == jogador_key:
                self.presentes.remove(jogador)
        for jogador in self.presentes_tela:
            if str(jogador[0:2]) == str(jogador_key):
                self.presentes_tela.remove(jogador)
        self.criar_partida(dados_partida, self.presentes_tela) 
    
    def adiciona_presente2(self, jogador, dados_jogador, dados_partida, partida_key):
        if jogador == []:
            self.__tela_cadastro.popup_ok('Selecione um jogador para adicionar.')
            self.criar_partida2(dados_partida, self.presentes_tela, partida_key, 'vazio')
        jogador_key = jogador[0][0:2]
        jogador = self.__sistema_geral.controlador_principal.jogadores.get(jogador_key)
        nome = jogador.nome
        numero = jogador.numero
        gols = (int(dados_jogador['go']))
        cartoes_amarelos = (int(dados_jogador['ca']))
        cartoes_vermelhos = (int(dados_jogador['cv']))
        jogador = Presente(nome, numero, gols, cartoes_amarelos, cartoes_vermelhos)
        qtd = 0
        presente = False
        if len(self.presentes) == 0:
            self.presentes.append(jogador)
            self.presentes_tela.append(jogador.numero + " " + jogador.nome)
        else:
            for i in self.presentes:
                if i.numero == jogador.numero:
                    presente = True
            if presente == True:
                qtd = qtd + 1
            if qtd == 0:
                self.presentes.append(jogador)
                self.presentes_tela.append(jogador.numero + " " + jogador.nome)
        self.criar_partida2(dados_partida, self.presentes_tela, partida_key, 'vazio')

    def retira_presente2(self, presente, dados_partida, partida_key):
        if presente == []:
            self.__tela_cadastro.popup_ok('Selecione um jogador para retirar.')
            self.criar_partida2(dados_partida, self.presentes_tela, partida_key, 'vazio')
        jogador_key = presente[0][0:2]
        for jogador in self.presentes:
            if jogador.numero == jogador_key:
                jogador_deletar = copy.copy(self.__sistema_geral.controlador_principal.jogadores.get(jogador_key))
                if jogador_deletar == None:
                    jogador_deletar == 'vazio'
                self.presentes.remove(jogador)
        for jogador in self.presentes_tela:
            if str(jogador[0:2]) == str(jogador_key):
                self.presentes_tela.remove(jogador)
        self.criar_partida2(dados_partida, self.presentes_tela, partida_key, jogador_deletar)
    
    def criar_partida2(self, dados_partida, presentes_tela, partida_key, jogador_deletar):
        jogadores = self.__sistema_geral.controlador_principal.listar_jogadores()
        button, values = self.__tela_cadastro.abre_tela(dados_partida, jogadores, presentes_tela)
        #Dados do imput
        local = 'Campo do Inter'
        mandante = 'Família Franzoni'
        adversario = values['1']
        gols_mandante = values['2']
        gols_adversario = values['3']
        data = values['4']
        dados_partida = {'data': data, 'gols_mandante': gols_mandante, 'gols_adversario': gols_adversario, 'adversario': adversario}
        if button == 'adiciona':
            gols = values['go']
            ca = values['ca']
            cv = values['cv']
            dados_jogador = {'go': gols, 'ca': ca, 'cv':cv}
            self.adiciona_presente2(values['jogador'], dados_jogador, dados_partida, dados_partida['data'])
        if button == 'retira':
            self.retira_presente2(values['presente'], dados_partida, dados_partida['data'])
        if button == None:
            self.finalizar()
        if button == 'back':
            self.voltar()
        #Valida data
        if data == '':
            self.__tela.popup_ok('Escolha a data.')
            dados_partida = {'data': '', 'gols_mandante': gols_mandante, 'gols_adversario': gols_adversario, 'adversario': adversario}
            self.criar_partida2(dados_partida, self.presentes_tela, partida_key)
        for partida in self.partidas.get_all():
            if partida.data == data and partida.data != partida_key:
                self.__tela.popup_ok('Já existe outra partida nessa data.')
                dados_partida = {'data': '', 'gols_mandante': gols_mandante, 'gols_adversario': gols_adversario, 'adversario': adversario}
                self.criar_partida2(dados_partida, self.presentes_tela, partida_key)
        #Ajeita Nome
        preposicoes = ['da', 'de', 'di', 'do', 'du', 'para']
        partes_nome = []
        for parte in adversario.split():
            if not parte in preposicoes:
                parte = parte.capitalize()
            partes_nome.append(parte)
        adversario = ' '.join(partes_nome)
        #Valida Resultado:
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        todos_int = True
        todos_int2 = True
        for gol in gols_mandante:
            if gol not in numeros:
                todos_int = False
        for gol in gols_adversario:
            if gol not in numeros:
                todos_int2 = False
        if todos_int == False or todos_int2 == False or gols_mandante == '' or gols_adversario == '':
            self.__tela_cadastro.popup_ok('Digite apenas números válidos no resultado da partida.')
            dados_partida = {'data': data, 'gols_mandante': '', 'gols_adversario': '', 'adversario': adversario}
            self.criar_partida2(dados_partida, self.presentes_tela, partida_key)
        if button == 'confirma':
            decisao = self.__tela_cadastro.confirm('Você tem certeza que deseja fazer essas alterações?')
            if decisao == 'Yes':
                self.__partidas.remove(partida_key)
                presentes = copy.copy(self.presentes)
                presentes_tela = copy.copy(self.presentes_tela)
                nova_partida = Partida(local, data, data[:2], data[3:5], data[6:10], gols_mandante, gols_adversario, mandante, adversario, presentes, presentes_tela)
                nova_partida.listar_gols()
                nova_partida.listar_cartoes_amarelos()
                nova_partida.listar_cartoes_vermelhos()
                self.partidas.add(nova_partida.data, nova_partida)
                lista_deletados = []
                lista_jogadores = []
                if jogador_deletar != 'vazio':
                    lista_deletados.append(jogador_deletar)
                for presente in self.presentes:
                    lista_jogadores.append(self.__sistema_geral.controlador_principal.jogadores.get(presente.numero))
                for jogador in lista_jogadores:
                    for partida in jogador.partidas:
                        if str(partida_key) == str(partida.data):
                            jogador.partidas.remove(partida)
                    jogador.partidas.append(nova_partida)
                    jogador.atualiza_gols()
                    jogador.atualiza_cartoes_amarelos()
                    jogador.atualiza_cartoes_vermelhos()
                    self.__sistema_geral.controlador_principal.jogadores.remove(jogador.numero)
                    self.__sistema_geral.controlador_principal.jogadores.add(jogador.numero, jogador)
                for jogador in lista_deletados:
                    if jogador != None:
                        for partida in jogador.partidas:
                            if str(partida_key) == str(partida.data):
                                jogador.partidas.remove(partida)
                        jogador.atualiza_gols()
                        jogador.atualiza_cartoes_amarelos()
                        jogador.atualiza_cartoes_vermelhos()
                        self.__sistema_geral.controlador_principal.jogadores.remove(jogador.numero)
                        self.__sistema_geral.controlador_principal.jogadores.add(jogador.numero, jogador)
                self.__tela.popup_ok('Partida alterada com sucesso!')
                self.voltar()
    
    def alterar_partida(self, partida):
        if partida == []:
            self.__tela.popup_ok('Você deve selecionar uma partida.')
            self.voltar()
        jogadores = self.__sistema_geral.controlador_principal.listar_jogadores()
        partida_key = partida[0][0:10]
        partida = self.__partidas.get(partida_key)
        dados_partida = {'data': partida.data, 'gols_mandante': partida.gols_mandante, 'gols_adversario': partida.gols_adversario, 'adversario': partida.adversario}
        button, values = self.__tela_cadastro.abre_tela(dados_partida, jogadores, partida.presentes_tela)
        for jogador in partida.presentes:
            self.__presentes.append(jogador)
        for jogador in partida.presentes_tela:
            self.__presentes_tela.append(jogador)
        #Dados do imput
        local = 'Campo do Inter'
        mandante = 'Família Franzoni'
        adversario = values['1']
        gols_mandante = values['2']
        gols_adversario = values['3']
        data = values['4']
        dados_partida = {'data': data, 'gols_mandante': gols_mandante, 'gols_adversario': gols_adversario, 'adversario': adversario}
        if button == 'adiciona':
            gols = values['go']
            ca = values['ca']
            cv = values['cv']
            dados_jogador = {'go': gols, 'ca': ca, 'cv':cv}
            self.adiciona_presente2(values['jogador'], dados_jogador, dados_partida, partida_key)
        if button == 'retira':
            self.retira_presente2(values['presente'], dados_partida, partida_key)
        if button == None:
            self.finalizar()
        if button == 'back':
            self.opcoes()
        #Valida data
        if data == '':
            self.__tela.popup_ok('Escolha a data.')
            dados_partida = {'data': '', 'gols_mandante': gols_mandante, 'gols_adversario': gols_adversario, 'adversario': adversario}
            self.criar_partida2(dados_partida, self.presentes_tela, partida_key, 'vazio')
        for partida in self.partidas.get_all():
            if partida.data == data and partida.data != partida_key:
                self.__tela.popup_ok('Já existe outra partida nessa data.')
                dados_partida = {'data': '', 'gols_mandante': gols_mandante, 'gols_adversario': gols_adversario, 'adversario': adversario}
                self.criar_partida2(dados_partida, self.presentes_tela, partida_key, 'vazio')
        #Ajeita Nome
        preposicoes = ['da', 'de', 'di', 'do', 'du', 'para']
        partes_nome = []
        for parte in adversario.split():
            if not parte in preposicoes:
                parte = parte.capitalize()
            partes_nome.append(parte)
        adversario = ' '.join(partes_nome)
        #Valida Resultado:
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        todos_int = True
        todos_int2 = True
        for gol in gols_mandante:
            if gol not in numeros:
                todos_int = False
        for gol in gols_adversario:
            if gol not in numeros:
                todos_int2 = False
        if todos_int == False or todos_int2 == False or gols_mandante == '' or gols_adversario == '':
            self.__tela_cadastro.popup_ok('Digite apenas números válidos no resultado da partida.')
            dados_partida = {'data': data, 'gols_mandante': '', 'gols_adversario': '', 'adversario': adversario}
            self.criar_partida2(dados_partida, self.presentes_tela, partida_key)
        if button == 'confirma':
            decisao = self.__tela_cadastro.confirm('Você tem certeza que deseja fazer essas alterações?')
            if decisao == 'Yes':
                self.partidas.remove(partida_key)
                presentes = copy.copy(self.presentes)
                presentes_tela = copy.copy(self.presentes_tela)
                nova_partida = Partida(local, data, data[:2], data[3:5], data[6:10], gols_mandante, gols_adversario, mandante, adversario, presentes, presentes_tela)
                nova_partida.listar_gols()
                nova_partida.listar_cartoes_amarelos()
                nova_partida.listar_cartoes_vermelhos()
                self.partidas.add(nova_partida.data, nova_partida)
                lista_jogadores = []
                for jogador in self.__sistema_geral.controlador_principal.jogadores.get_all():
                    for presente in self.presentes:
                        if jogador.nome == presente:
                            lista_jogadores.append(jogador)
                for jogador in lista_jogadores:
                    for partida in jogador.partidas:
                        if partida.data == partida_key:
                            jogador.partidas.remove(partida)
                    jogador.partidas.append(nova_partida)
                    jogador.atualiza_gols()
                    jogador.atualiza_cartoes_amarelos()
                    jogador.atualiza_cartoes_vermelhos()
                    self.__sistema_geral.controlador_principal.jogadores.remove(jogador.numero)
                    self.__sistema_geral.controlador_principal.jogadores.add(jogador.numero, jogador)
                self.__tela.popup_ok('Partida alterada com sucesso!')
                self.voltar()
                  
    def excluir_partida(self, partida):
        if partida == []:
            self.__tela.popup_ok('Você deve selecionar uma partida.')
            self.voltar()
        partida_key = partida[0][0:10]
        quer_apagar = self.__tela.confirm('Você tem certeza que deseja excluir a partida ?')
        if quer_apagar == 'Yes':
            lista_jogadores = []
            for jogador in self.__sistema_geral.controlador_principal.jogadores.get_all():
                lista_jogadores.append(jogador)
            for jogador in lista_jogadores:
                for partida in jogador.partidas:
                    if partida.data == partida_key:
                        jogador.partidas.remove(partida)
                jogador.atualiza_gols()
                jogador.atualiza_cartoes_amarelos()
                jogador.atualiza_cartoes_vermelhos()
                self.__sistema_geral.controlador_principal.jogadores.remove(jogador.numero)
                self.__sistema_geral.controlador_principal.jogadores.add(jogador.numero, jogador)
            self.__partidas.remove(partida_key)
            self.voltar()
        else:
            self.voltar()