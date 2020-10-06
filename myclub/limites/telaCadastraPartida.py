import PySimpleGUI as sg
from .telaAbstract import TelaAbstract


class TelaCadastraPartida(TelaAbstract):
    def __init__(self):
        self.__window = None

    def configura(self, dados_partida, jogadores, presentes):
        sg.ChangeLookAndFeel('SystemDefault'),
        layout = [
            [sg.CalendarButton('Data:', target='4', button_color=('red', 'white'), format=('%d/%m/%Y')), sg.InputText(dados_partida['data'], key='4', visible=True, disabled=True, size=(9, 1)), sg.Checkbox('Casa', key='5', font='Arial 12', default=True), sg.Checkbox('Fora', key='6', font='Arial 12')],
            [sg.Text('')],
            [sg.Text('Inter do Carianos', size=(14, 1)), sg.InputText(dados_partida['gols_mandante'], size =(2,1), key='2'), sg.Text(' x ', size=(2, 1)), sg.InputText(dados_partida['gols_adversario'], size =(2,1), key='3'), sg.Text(' ', size=(1, 1)), sg.InputText(dados_partida['adversario'], size=(14, 1), key='1')],
            [sg.Text('')],
            [sg.Text('              Plantel'), sg.Text('                           Presentes')],
            [sg.Listbox(values=(jogadores), size=(43, 29), font='Fixedsys 15', key='jogador'), sg.Listbox(values=(presentes), size=(43, 29), font='Fixedsys 15', key='presente')],
            [sg.Text('Go:'), sg.Spin(values=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99'), initial_value='0', key='go'), sg.Text('Ca:'), sg.Spin(values=('0','1','2'), initial_value='0', key='ca'), sg.Text('Cv:'), sg.Spin(values=('0','1'), initial_value='0', key='cv'), sg.Text(' '), sg.Submit('Adicionar', font='Arial 12', size=(18, 1), key='adiciona'), sg.Submit('Retirar', font='Arial 12', size=(18, 1), key='retira')],
            [sg.Submit('Confirmar', font='Arial 12', size=(10, 1), key='confirma')]
        ]
        layout.extend(self.voltar())
        self.__window = sg.Window('Partida', element_justification='left', size=(800, 850), font='Arial 24', icon='icon.ico').Layout(layout)

    def abre_tela(self, dados_partida, jogadores, presentes):
        self.configura(dados_partida, jogadores, presentes)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values