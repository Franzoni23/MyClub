import PySimpleGUI as sg
from .telaAbstract import TelaAbstract

class TelaInicial(TelaAbstract):
    def __init__(self):
        self.__window = None

    def configura(self, jogadores):
        sg.ChangeLookAndFeel('SystemDefault'),
        layout = [
            [sg.Text('Jogadores', font='Arial 28'), sg.Text('                                                    Id   ', font='Arial 12'), sg.Text('Po    ', font='Arial 12'), sg.Submit('Pj', font='Arial 10', size=(6, 1), key='4'), sg.Submit('Go', font='Arial 10', size=(6, 1), key='5'), sg.Submit('Ca', font='Arial 10', size=(6, 1), key='6'), sg.Submit('Cv', font='Arial 10', size=(6, 1), key='7')],
            [sg.Listbox(values=(jogadores), size=(140, 45), font='Fixedsys 15', pad=(None), key='jogador')],
            [sg.Text('Legenda: Id = Idade, Po = Posição, Pj = Partidas jogadas, Go = Gols, Ca = Cartões Amarelos, Cv = Cartões Vermelhos.', font='Arial 10')],
            [sg.Submit('Criar', font='Arial 10', size=(5, 1), key='1'),
            sg.Submit('Excluir', font='Arial 10', size=(5, 1), key='2'),
            sg.Submit('Alterar', font='Arial 10', size=(5, 1), key='3')]
        ]
        self.__window = sg.Window('MyClub', element_justification='l', size=(800, 850)).Layout(layout)

    def abre_tela(self, jogadores):
        self.configura(jogadores)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values