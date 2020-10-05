import PySimpleGUI as sg
from .telaAbstract import TelaAbstract

class TelaPartidasJogador(TelaAbstract):
    def __init__(self):
        self.__window = None

    def configura(self, partidas):
        sg.ChangeLookAndFeel('SystemDefault'),
        layout = [
            [sg.Listbox(values=(partidas), size=(140, 50), font='Fixedsys 15', pad=(None), key='partida')],
            [sg.Submit('Voltar', font='Arial 10', size=(5, 1), key='back')]
        ]
        self.__window = sg.Window('Partidas do Jogador', element_justification='l', size=(800, 850), icon='icon.ico').Layout(layout)

    def abre_tela(self, partidas):
        self.configura(partidas)
        button, values = self.__window.Read()
        self.__window.Close()
        return (button), values