import PySimpleGUI as sg
from abc import ABC, abstractmethod


class TelaAbstract(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @staticmethod
    def voltar():
        layout_extra = [
            [sg.Submit('Voltar', font='Arial 10', size=(5, 1), key='back')],
        ]
        return layout_extra

    @staticmethod
    def confirm(mensagem):
        return sg.PopupYesNo(mensagem, title='Confirmação')

    @staticmethod
    def popup_ok(mensagem):
        return sg.PopupOK(mensagem, title='Aviso')