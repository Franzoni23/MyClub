from myclub.entidades.jogador import Jogador
from myclub.DAO.JogadoresDAO import JogadoresDAO
from myclub.limites.telaInicial import TelaInicial
from myclub.limites.telaGols import TelaGols
from myclub.limites.telaCartoesAmarelos import TelaCartoesAmarelos
from myclub.limites.telaCartoesVermelhos import TelaCartoesVermelhos
from myclub.limites.telaCadastraJogador import TelaCadastraJogador
import sys
import datetime


class ControladorPrincipal:
    def __init__(self, sistema_geral):
        self.__sistema_geral = sistema_geral
        self.__tela = TelaInicial()
        self.__tela_gols = TelaGols()
        self.__tela_cartoes_amarelos = TelaCartoesAmarelos()
        self.__tela_cartoes_vermelhos = TelaCartoesVermelhos()
        self.__tela_cadastro = TelaCadastraJogador()
        self.__jogadores = JogadoresDAO()

    @property
    def jogadores(self):
        return self.__jogadores
    
    def finalizar(self):
        sys.exit(0)

    def voltar(self):
        self.opcoes()
    
    def listar_goleiros(self):
        lista_print = []
        for jogador in self.__jogadores.get_all():  
            if jogador.posicao == 'Goleiro':
                cartoes_amarelos = jogador.cartoes_amarelos
                cartoes_vermelhos = jogador.cartoes_vermelhos
                gols = jogador.gols
                nome = jogador.nome.ljust(46)
                idade = jogador.idade
                posicao = 'G'
                qtd_partidas = jogador.qtd_partidas
                lista_print.append(jogador.numero + " " + nome + str(idade) + "    " + str(posicao) + "       " + str(qtd_partidas) + "     " + str(gols) + "     " + str(cartoes_amarelos) + "     " + str(cartoes_vermelhos))                      
        lista_print.sort()
        return lista_print

    def listar_laterais(self):
        lista_print = []
        for jogador in self.__jogadores.get_all():  
            if jogador.posicao == 'Lateral':
                cartoes_amarelos = jogador.cartoes_amarelos
                cartoes_vermelhos = jogador.cartoes_vermelhos
                gols = jogador.gols
                nome = jogador.nome.ljust(46)
                idade = jogador.idade
                posicao = 'L'
                qtd_partidas = jogador.qtd_partidas
                lista_print.append(jogador.numero + " " + nome + str(idade) + "    " + str(posicao) + "       " + str(qtd_partidas) + "     " + str(gols) + "     " + str(cartoes_amarelos) + "     " + str(cartoes_vermelhos))                      
        lista_print.sort()
        return lista_print

    def listar_zagueiros(self):
        lista_print = []
        for jogador in self.__jogadores.get_all():  
            if jogador.posicao == 'Zagueiro':
                cartoes_amarelos = jogador.cartoes_amarelos
                cartoes_vermelhos = jogador.cartoes_vermelhos
                gols = jogador.gols
                nome = jogador.nome.ljust(46)
                idade = jogador.idade
                posicao = 'Z'
                qtd_partidas = jogador.qtd_partidas
                lista_print.append(jogador.numero + " " + nome + str(idade) + "    " + str(posicao) + "       " + str(qtd_partidas) + "     " + str(gols) + "     " + str(cartoes_amarelos) + "     " + str(cartoes_vermelhos))                        
        lista_print.sort()
        return lista_print

    def listar_volantes(self):
        lista_print = []
        for jogador in self.__jogadores.get_all():  
            if jogador.posicao == 'Volante':
                cartoes_amarelos = jogador.cartoes_amarelos
                cartoes_vermelhos = jogador.cartoes_vermelhos
                gols = jogador.gols
                nome = jogador.nome.ljust(46)
                idade = jogador.idade
                posicao = 'V'
                qtd_partidas = jogador.qtd_partidas
                lista_print.append(jogador.numero + " " + nome + str(idade) + "    " + str(posicao) + "       " + str(qtd_partidas) + "     " + str(gols) + "     " + str(cartoes_amarelos) + "     " + str(cartoes_vermelhos))                        
        lista_print.sort()
        return lista_print

    def listar_meias(self):
        lista_print = []
        for jogador in self.__jogadores.get_all():  
            if jogador.posicao == 'Meia':
                cartoes_amarelos = jogador.cartoes_amarelos
                cartoes_vermelhos = jogador.cartoes_vermelhos
                gols = jogador.gols
                nome = jogador.nome.ljust(46)
                idade = jogador.idade
                posicao = 'M'
                qtd_partidas = jogador.qtd_partidas
                lista_print.append(jogador.numero + " " + nome + str(idade) + "    " + str(posicao) + "       " + str(qtd_partidas) + "     " + str(gols) + "     " + str(cartoes_amarelos) + "     " + str(cartoes_vermelhos))                      
        lista_print.sort()
        return lista_print

    def listar_atacantes(self):
        lista_print = []
        for jogador in self.__jogadores.get_all():  
            if jogador.posicao == 'Atacante':
                cartoes_amarelos = jogador.cartoes_amarelos
                cartoes_vermelhos = jogador.cartoes_vermelhos
                gols = jogador.gols
                nome = jogador.nome.ljust(46)
                idade = jogador.idade
                posicao = 'A'
                qtd_partidas = jogador.qtd_partidas
                lista_print.append(jogador.numero + " " + nome + str(idade) + "    " + str(posicao) + "       " + str(qtd_partidas) + "     " + str(gols) + "     " + str(cartoes_amarelos) + "     " + str(cartoes_vermelhos))                       
        lista_print.sort()
        return lista_print
    
    def listar_jogadores(self):
        lista_goleiros = self.listar_goleiros()
        lista_laterais = self.listar_laterais()
        lista_zagueiros = self.listar_zagueiros()
        lista_volantes = self.listar_volantes()
        lista_meias = self.listar_meias()
        lista_atacantes = self.listar_atacantes()
        lista_print = lista_goleiros + lista_laterais + lista_zagueiros + lista_volantes + lista_meias + lista_atacantes
        return lista_print
    
    def listar_gols(self):
        lista_print = []
        for jogador in self.jogadores.get_all():
                lista_print.append(jogador.gols + ' - ' + jogador.nome)
        lista_print.sort(reverse=True)
        return lista_print

    def listar_cartoes_amarelos(self):
        lista_print = []
        for jogador in self.jogadores.get_all():
                lista_print.append(jogador.cartoes_amarelos + ' - ' + jogador.nome)
        lista_print.sort(reverse=True)
        return lista_print

    def listar_cartoes_vermelhos(self):
        lista_print = []
        for jogador in self.jogadores.get_all():
                lista_print.append(jogador.cartoes_vermelhos + ' - ' + jogador.nome)
        lista_print.sort(reverse=True)
        return lista_print
    
    def gols(self):
        gols = self.listar_gols()
        button, values = self.__tela_gols.abre_tela(gols)
        if button == None:
            self.finalizar()
        if button == 'back':
            self.voltar()

    def cartoes_amarelos(self):
        cartoes_amarelos = self.listar_cartoes_amarelos()
        button, values = self.__tela_cartoes_amarelos.abre_tela(cartoes_amarelos)
        if button == None:
            self.finalizar()
        if button == 'back':
            self.voltar()

    def cartoes_vermelhos(self):
        cartoes_vermelhos = self.listar_cartoes_vermelhos()
        button, values = self.__tela_cartoes_vermelhos.abre_tela(cartoes_vermelhos)
        if button == None:
            self.finalizar()
        if button == 'back':
            self.voltar()
    
    def opcoes(self):
        jogadores = self.listar_jogadores()
        opcoes = {'1': self.criar_jogador, '2': self.excluir_jogador, '3':self.alterar_jogador, '4':self.__sistema_geral.partidas_jogadas, '5':self.__sistema_geral.gols, '6':self.__sistema_geral.cartoes_amarelos, '7':self.__sistema_geral.cartoes_vermelhos, None:self.finalizar}
        button, values = self.__tela.abre_tela(jogadores)
        opçao_escolhida = opcoes[button]
        if button == '1':
            opçao_escolhida = opcoes[button]('vazio')
        if button == '2' or button == '3' or button == '4' or button == '5' or button == '6' or button == '7':
            opçao_escolhida = opcoes[button](values['jogador'])
        opçao_escolhida()
        
    def criar_jogador(self, dados_jogador):
        if dados_jogador == 'vazio':
            dados = {'nome': '', 'numero': '', 'dia': '', 'mes': '', 'ano': '', 'posicao': ''}
        else:
            dados = dados_jogador
        button, values = self.__tela_cadastro.abre_tela(dados)
        if button == None:
            self.finalizar()
        if button == 'back':
            self.voltar()
        #Dados do imput
        nome = values['1']
        numero = values['2']
        dia = values['3']
        mes = values['4']
        ano = values['5']
        posicao = values['6']
        #Valida Nome
        if nome == '':
            self.__tela.popup_ok('Preencha o nome.')
            dados_jogador = {'nome': nome, 'numero': numero, 'dia': dia, 'mes': mes, 'ano': ano, 'posicao': posicao}
            self.criar_jogador(dados_jogador)
        #Ajeita Nome
        preposicoes = ['da', 'de', 'di', 'do', 'du', 'para']
        partes_nome = []
        for parte in nome.split():
            if not parte in preposicoes:
                parte = parte.capitalize()
            partes_nome.append(parte)
        nome = ' '.join(partes_nome)
        #Valida Numero
        numeros_validos = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99']
        if numero not in numeros_validos:
            self.__tela.popup_ok('Número inválido.')
            dados_jogador = {'nome': nome, 'numero': '', 'dia': dia, 'mes': mes, 'ano': ano, 'posicao': posicao}
            self.criar_jogador(dados_jogador)
        for jogador in self.jogadores.get_all():
            if nome != jogador.nome and numero == jogador.numero:
                self.__tela.popup_ok('Número já está em uso.')
                dados_jogador = {'nome': nome, 'numero': numero, 'dia': dia, 'mes': mes, 'ano': ano, 'posicao': posicao}
                self.criar_jogador(dados_jogador)
        #Valida Nascimento
        if dia not in ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']:
            self.__tela.popup_ok('Dia inválido')
            dados_jogador = {'nome': nome, 'numero': numero, 'dia': '', 'mes': mes, 'ano': ano, 'posicao': posicao}
            self.criar_jogador(dados_jogador)
        if mes not in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            self.__tela.popup_ok('Mês inválido')
            dados_jogador = {'nome': nome, 'numero': numero, 'dia': dia, 'mes': '', 'ano': ano, 'posicao': posicao}
            self.criar_jogador(dados_jogador)
        if ano not in ['1950','1951','1952','1953','1954','1955','1956','1957','1958','1959','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']:
            self.__tela.popup_ok('Ano inválido')
            dados_jogador = {'nome': nome, 'numero': numero, 'dia': dia, 'mes': mes, 'ano': '', 'posicao': posicao}
            self.criar_jogador(dados_jogador)
        #Valida Posição
        posicoes_validas = ['Goleiro', 'Lateral', 'Zagueiro', 'Volante', 'Meia', 'Atacante']
        if posicao not in posicoes_validas:
            self.__tela.popup_ok('Posição inválida.')
            dados_jogador = {'nome': nome, 'numero': '', 'dia': dia, 'mes': mes, 'ano': ano, 'posicao': ''}
            self.criar_jogador(dados_jogador)  
        nascimento = dia + "/" + mes + "/" + ano
        novo_jogador = Jogador(nome, numero, nascimento, posicao)
        self.jogadores.add(novo_jogador.numero, novo_jogador)
        self.__tela.popup_ok('Jogador registrado com sucesso!')
        self.voltar()

    def excluir_jogador(self, jogador):
        if jogador == []:
            self.__tela.popup_ok('Você deve selecionar um jogador.')
            self.voltar()
        jogador_key = jogador[0][0:2]
        quer_apagar = self.__tela.confirm('Você tem certeza que deseja excluir o jogador ?')
        if quer_apagar == 'Yes':
            self.__jogadores.remove(jogador_key)
            self.voltar()
        else:
            self.voltar()

    def alterar_jogador(self, jogador):
        if jogador == []:
            self.__tela.popup_ok('Você deve selecionar um jogador.')
            self.voltar()
        jogador_key = jogador[0][0:2]
        jogador = self.__jogadores.get(jogador_key)
        dados_jogador = {'nome': jogador.nome, 'numero': jogador.numero, 'dia': jogador.nascimento[:2], 'mes': jogador.nascimento[3:5], 'ano': jogador.nascimento[6:10], 'posicao': jogador.posicao}
        button, values = self.__tela_cadastro.abre_tela(dados_jogador)
        if button == None:
            self.finalizar()
        if button == 'back':
            self.voltar()
        if button == 'confirma':
            decisao = self.__tela_cadastro.confirm('Você tem certeza que deseja fazer essas alterações?')
            #Dados do imput
            nome = values['1']
            numero = values['2']
            dia = values['3']
            mes = values['4']
            ano = values['5']
            posicao = values['6']
            if decisao == 'Yes':
                self.__jogadores.remove(jogador_key)
                #Valida Nome
                if nome == '':
                    self.__tela.popup_ok('Preencha o nome.')
                    dados_jogador = {'nome': nome, 'numero': numero, 'dia': dia, 'mes': mes, 'ano': ano, 'posicao': posicao}
                    self.criar_jogador(dados_jogador)
                #Ajeita Nome
                preposicoes = ['da', 'de', 'di', 'do', 'du', 'para']
                partes_nome = []
                for parte in nome.split():
                    if not parte in preposicoes:
                        parte = parte.capitalize()
                    partes_nome.append(parte)
                nome = ' '.join(partes_nome)
                #Valida Numero
                numeros_validos = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99']
                if numero not in numeros_validos:
                    self.__tela.popup_ok('Número inválido.')
                    dados_jogador = {'nome': nome, 'numero': '', 'dia': dia, 'mes': mes, 'ano': ano, 'posicao': posicao}
                for jogador in self.jogadores.get_all():
                    if nome != jogador.nome and numero == jogador.numero:
                        self.__tela.popup_ok('Número já está em uso.')
                        dados_jogador = {'nome': nome, 'numero': numero, 'dia': dia, 'mes': mes, 'ano': ano, 'posicao': posicao}
                        self.criar_jogador(dados_jogador)
                #Valida Nascimento
                if dia not in ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']:
                    self.__tela.popup_ok('Dia inválido')
                    dados_jogador = {'nome': nome, 'numero': numero, 'dia': '', 'mes': mes, 'ano': ano, 'posicao': posicao}
                    self.criar_jogador(dados_jogador)
                if mes not in ['01','02','03','04','05','06','07','08','09','10','11','12']:
                    self.__tela.popup_ok('Mês inválido')
                    dados_jogador = {'nome': nome, 'numero': numero, 'dia': dia, 'mes': '', 'ano': ano, 'posicao': posicao}
                    self.criar_jogador(dados_jogador)
                if ano not in ['1950','1951','1952','1953','1954','1955','1956','1957','1958','1959','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']:
                    self.__tela.popup_ok('Ano inválido')
                    dados_jogador = {'nome': nome, 'numero': numero, 'dia': dia, 'mes': mes, 'ano': '', 'posicao': posicao}
                    self.criar_jogador(dados_jogador)
                #Valida Posição
                posicoes_validas = ['Goleiro', 'Lateral', 'Zagueiro', 'Volante', 'Meia', 'Atacante']
                if posicao not in posicoes_validas:
                    self.__tela.popup_ok('Posição inválida.')
                    dados_jogador = {'nome': nome, 'numero': '', 'dia': dia, 'mes': mes, 'ano': ano, 'posicao': ''}
                    self.criar_jogador(dados_jogador)
                nascimento = dia + "/" + mes + "/" + ano
                novo_jogador = Jogador(nome, numero, nascimento, posicao)
                self.__jogadores.add(novo_jogador.numero, novo_jogador)
                self.__tela.popup_ok('Jogador registrado com sucesso!')
                self.voltar()
            else:
                dados_jogador = {'nome': nome, 'numero': numero, 'dia': dia, 'mes': mes, 'ano': ano, 'posicao': posicao}
                self.criar_jogador(dados_jogador)