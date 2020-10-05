import PySimpleGUI as sg
from .telaAbstract import TelaAbstract

class TelaGols(TelaAbstract):
    def __init__(self):
        self.__window = None

    def configura(self, gols):
        sg.ChangeLookAndFeel('SystemDefault'),
        layout = [
            [sg.Listbox(values=(gols), size=(140, 50), font='Fixedsys 15', pad=(None), key='partida')],
            [sg.Submit('Voltar', font='Arial 10', size=(5, 1), key='back')]
        ]
        self.__window = sg.Window('Artilharia', element_justification='l', size=(800, 850), icon='icon.ico').Layout(layout)

    def abre_tela(self, gols):
        self.configura(gols)
        button, values = self.__window.Read()
        self.__window.Close()
        return (button), values