from PySide6.QtCore import QDate
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
import datetime as dt

from PageModels.InserirManager import InserirManager
# from PageModels.AlterarManager import AlterarManager
# from PageModels.BuscarManager import BuscarManager

from views.MainWindowUi import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Projeto 1 Estrutura de Dados")
        # app_icon = QIcon(u"style/icon.png")
        # self.setWindowIcon(app_icon)

        ##################################################################################################
        # ESTILIZAÇÃO
        self.setStyleSheet("""
            QLineEdit[readOnly="true"] { background-color: black; color: #ffffff; }
            QDateTimeEdit[readOnly="true"] { background-color: black; color: #ffffff; }
        """)
        ##################################################################################################

        ##################################################################################################
        # PÁGINAS/VARIÁVEIS DO SISTEMA
        self.btn_tela_inserir.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_inserir))
        self.inserir_manager = InserirManager(self)
        
        self.btn_tela_alterar.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_editar))
        # self.alterar_manager = AlterarManager(self)
        
        self.btn_tela_buscar.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_buscas))
        # self.buscas_manager = BuscarManager(self)
    
        ##################################################################################################

        ##################################################################################################
        # EVENTOS TELA INSERIR
        # Botões da tela Inserir
        self.btn_limpar_f_inserir.clicked.connect(lambda: self.inserir_manager.clear_inputs(0))
        self.btn_limpar_p_inserir.clicked.connect(lambda: self.inserir_manager.clear_inputs(1))
        self.btn_inserir_f.clicked.connect(lambda: self.inserir_manager.inserir_dados(0))
        self.btn_p_inserir.clicked.connect(lambda: self.inserir_manager.inserir_dados(1))

        # Variáveis da página Cadastro
        # cod_inputs = [self.input_cad_grupo, self.input_cad_subgrupo, self.input_cad_vers, self.input_cad_id]
        # for inp in cod_inputs:
        #     inp.textChanged.connect(lambda: self.cadastro_manager.print_cod_produto(cod_inputs))
        ##################################################################################################

        ##################################################################################################
        # EVENTOS TELA CONSULTA
        # Botões da tela Consulta
        # self.btn_cons_buscar.clicked.connect(lambda: self.consulta_manager.to_query())
        # self.btn_cons_limpar.clicked.connect(lambda: self.consulta_manager.clear_query_inputs())
        # self.btn_cons_gerar_xlsx.clicked.connect(lambda: self.consulta_manager.generate_xlsx_from_query())
        # self.btn_cons_limpar_table.clicked.connect(lambda: self.consulta_manager.clear_table())

        # self.ck_filtrar_cod.stateChanged.connect(lambda: self.consulta_manager.ck_cons_cod_changer())

        # # Variáveis da página Consulta
        # self.today = dt.datetime.today()
        # self.date_end.setDate(QDate(self.today.year, self.today.month, self.today.day))
        # ##################################################################################################

        # ##################################################################################################
        # # EVENTOS TELA FAMILIAS
        # # Botões da tela Familias
        # self.btn_fam_criar.clicked.connect(lambda: self.familias_manager.criar_familia())
        # self.btn_fam_editar.clicked.connect(lambda: self.familias_manager.editar_familias())
        # self.btn_fam_atualizar.clicked.connect(lambda: self.familias_manager.query_familias())
        # self.btn_fam_del.clicked.connect(lambda: self.familias_manager.deletar_familia())
        # self.btn_fam_limpar.clicked.connect(lambda: self.familias_manager.limpar_inputs_edit())

        # # Variáveis da página Famílias
        # self.familias_manager.query_familias()
        # ##################################################################################################
