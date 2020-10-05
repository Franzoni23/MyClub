from myclub.entidades.jogador import Jogador
from .AbstractDAO import DAO


class JogadoresDAO(DAO):
    def __init__(self):
        super().__init__('jogadores.pkl')

    def __add__(self, jogador: Jogador):
        if isinstance(jogador, Jogador):
            super().add(jogador.numero, jogador)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
