import PySimpleGUI as sg
from .telaAbstract import TelaAbstract


class TelaCadastraJogador(TelaAbstract):
    def __init__(self):
        self.__window = None

    def configura(self, dados_jogador):
        sg.ChangeLookAndFeel('SystemDefault'),
        layout = [
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(dados_jogador['nome'], key='1')],
            [sg.Text('Número:', size=(15, 1)), sg.Combo(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99'], default_value=dados_jogador['numero'], key='2')],
            [sg.Text('Data de nascimento:', size=(15, 1)), sg.Combo(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'], default_value=dados_jogador['dia'], key='3'), sg.Combo(['01','02','03','04','05','06','07','08','09','10','11','12'], default_value=dados_jogador['mes'], key='4'), sg.Combo(['1950','1951','1952','1953','1954','1955','1956','1957','1958','1959','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'], default_value=dados_jogador['ano'], key='5')],
            [sg.Text('Posição:', size=(15, 1)), sg.Combo(['Goleiro', 'Lateral', 'Zagueiro', 'Volante', 'Meia', 'Atacante'], default_value=dados_jogador['posicao'], key='6')],
            [sg.Submit('Confirmar', font='Arial 12', size=(10, 1), key='confirma')]
        ]
        layout.extend(self.voltar())
        self.__window = sg.Window('Jogadores', element_justification='left', size=(800, 850), font='Arial 24', icon='icon.ico').Layout(layout)

    def abre_tela(self, dados_jogador):
        self.configura(dados_jogador)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values