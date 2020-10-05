import PySimpleGUI as sg
from .telaAbstract import TelaAbstract

class TelaCartoesAmarelos(TelaAbstract):
    def __init__(self):
        self.__window = None

    def configura(self, cartoes_amarelos):
        sg.ChangeLookAndFeel('SystemDefault'),
        layout = [
            [sg.Text('Cartões Amarelos', font='Arial 28')],
            [sg.Listbox(values=(cartoes_amarelos), size=(140, 46), font='Fixedsys 15', pad=(None), key='partida')],
            [sg.Submit('Voltar', font='Arial 10', size=(5, 1), key='back')]
        ]
        self.__window = sg.Window('Cartões Amarelos', element_justification='l', size=(800, 850), icon='icon.ico').Layout(layout)

    def abre_tela(self, cartoes_amarelos):
        self.configura(cartoes_amarelos)
        button, values = self.__window.Read()
        self.__window.Close()
        return (button), values