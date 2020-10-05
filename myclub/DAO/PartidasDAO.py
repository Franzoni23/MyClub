from myclub.entidades.partida import Partida
from .AbstractDAO import DAO


class PartidasDAO(DAO):
    def __init__(self):
        super().__init__('partidas.pkl')

    def __add__(self, partida: Partida):
        if isinstance(partida, Partida):
            super().add(partida.data, partida)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
