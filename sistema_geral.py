from myclub.controladores.controladorPrincipal import ControladorPrincipal
from myclub.controladores.controladorPartida import ControladorPartida
import PySimpleGUI as psg


class SistemaGeral:
    def __init__(self):
        self.__controlador_principal = ControladorPrincipal(self)
        self.__controlador_partida = ControladorPartida(self)

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def controlador_partida(self):
        return self.__controlador_partida

    def inicio(self):
        self.controlador_principal.opcoes()

    def partidas_jogadas(self, jogador):
        if jogador == []:
            self.controlador_partida.opcoes()
        else:
            jogador_key = jogador[0][0:2]
            self.controlador_partida.partidas_jogador(jogador_key)

    def gols(self, jogador):
        if jogador == []:
            self.controlador_principal.gols()
        else:
            jogador_key = jogador[0][0:2]
            self.controlador_partida.gols_jogador(jogador_key)
    
    def cartoes_amarelos(self, jogador):
        if jogador == []:
            self.controlador_principal.cartoes_amarelos()
        else: 
            jogador_key = jogador[0][0:2]
            self.controlador_partida.cartoes_amarelos_jogador(jogador_key)

    def cartoes_vermelhos(self, jogador):
        if jogador == []:
            self.controlador_principal.cartoes_vermelhos()
        else: 
            jogador_key = jogador[0][0:2]
            self.controlador_partida.cartoes_vermelhos_jogador(jogador_key)

#Limitar gols, deixando igual a soma de presente.gols
#Adicionar adversarios em uma lista.

if __name__ == "__main__":
    sg = SistemaGeral()
    sg.inicio()