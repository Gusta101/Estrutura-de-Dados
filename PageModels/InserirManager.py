from PySide6.QtWidgets import QLineEdit, QDateEdit, QTreeWidget, QTextBrowser, QTreeWidgetItem, QDoubleSpinBox, QComboBox, QPushButton
from PySide6.QtCore import QDate

from models import Funcionario
from models import Projeto

from utils.data_utils import inserir_funcionario, inserir_projeto


class InserirManager:
    def __init__(self, main_page):
        self.main_page = main_page
        
        self.text_result = ""
        
        ###################################################################################################################################
        
        # Items da página Cadastro
        self.input_f_nome = self.main_page.findChild(QLineEdit, 'input_f_nome')
        self.input_f_n_func = self.main_page.findChild(QLineEdit, 'input_f_n_func')
        self.input_f_salario = self.main_page.findChild(QLineEdit, 'input_f_salario')
        self.input_p_nome = self.main_page.findChild(QLineEdit, 'input_p_nome')
        self.input_p_meses = self.main_page.findChild(QLineEdit, 'input_p_meses')
        self.input_p_valor_est = self.main_page.findChild(QLineEdit, 'input_p_valor_est')
        self.input_p_n_func = self.main_page.findChild(QLineEdit, 'input_p_n_func')
        self.date_p_inicio = self.main_page.findChild(QDateEdit, 'date_p_inicio')
        self.data_p_termino = self.main_page.findChild(QDateEdit, 'data_p_termino')

        self.log_inserir = self.main_page.findChild(QTextBrowser, 'log_inserir')

        ###################################################################################################################################

    # FUNÇÕES DA TELA INSERIR
    # Remove os valores das caixas de texto da tela Inserir, conforme a seção indicada (0 => funcionário, 1 => Projeto)
    def clear_inputs(self, tipo):
        if tipo == 0:
            inputs = [self.input_f_nome, self.input_f_n_func, self.input_f_salario]
        elif tipo == 1:
            inputs = [self.input_p_nome, self.input_p_meses, self.input_p_valor_est, self.input_p_n_func]
            self.date_p_inicio.setDate(QDate(QDate(2000, 0o1, 0o1)))
            self.data_p_termino.setDate(QDate(QDate(2000, 0o1, 0o1)))
        for inp in inputs:
            inp.setText("")
            
    # Envia as informações da tela para as funções de inserção em data_utils.py
    def inserir_dados(self, tipo):
        if tipo == 0:
            dados_func = [
                self.input_f_nome.text(),
                self.input_f_n_func.text(),
                self.input_f_salario.text(),
            ]
            response = inserir_funcionario(dados_func)
            if response:
                self.text_result += f'Funcionário N {dados_func[1]} inserido com sucesso, vetor atual:\n'
                self.text_result += response
            else:
                self.text_result += "Não foi possível inserir"
        elif tipo == 1:
            dados_proj = [
                self.input_p_nome.text(),
                self.input_p_meses.text(),
                self.input_p_valor_est.text(),
                self.input_p_n_func.text(),
                self.date_p_inicio.text(),
                self.data_p_termino.text(),
            ]
            self.text_result = inserir_projeto(dados_proj)
        
        self.print_log()
    
    def print_log(self):
        self.log_inserir.setText(self.text_result)
        self.text_result = ""
