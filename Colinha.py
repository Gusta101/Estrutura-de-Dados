from PySide6.QtCore import QDate
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
import datetime as dt

from PageModels.CadastroManager import CadastroManager
from PageModels.ConsultaManager import ConsultaManager
from PageModels.FamiliasManager import FamiliasManager
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gestão de produtos")
        app_icon = QIcon(u"style/icon.png")
        self.setWindowIcon(app_icon)

        ##################################################################################################
        # ESTILIZAÇÃO
        self.setStyleSheet("""
            QLineEdit[readOnly="true"] { background-color: black; color: #ffffff; }
            QDateTimeEdit[readOnly="true"] { background-color: black; color: #ffffff; }
        """)
        ##################################################################################################

        ##################################################################################################
        # PÁGINAS/VARIÁVEIS DO SISTEMA
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_home))

        self.btn_menu_consulta.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_consulta))
        self.btn_menu_consulta.clicked.connect(lambda: self.consulta_manager.update_combo_familias())
        self.consulta_manager = ConsultaManager(self)

        self.btn_menu_cadastro.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_cadastro))
        self.btn_menu_cadastro.clicked.connect(lambda: self.cadastro_manager.update_combo_familias())
        self.cadastro_manager = CadastroManager(self)

        self.btn_menu_familias.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_familias))
        self.familias_manager = FamiliasManager(self)

        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_sobre))
        ##################################################################################################

        ##################################################################################################
        # EVENTOS TELA CADASTRO
        # Botões da tela Cadastro
        self.btn_cad_adc_item.clicked.connect(lambda: self.cadastro_manager.add_produto_queue())
        self.btn_cad_limpar_queue.clicked.connect(lambda: self.cadastro_manager.clear_queue())
        self.btn_gerar_xl.clicked.connect(lambda: self.cadastro_manager.generate_xlsx_from_queue())
        self.btn_cad_enviar.clicked.connect(lambda: self.cadastro_manager.send_queue_to_omie())

        # Variáveis da página Cadastro
        cod_inputs = [self.input_cad_grupo, self.input_cad_subgrupo, self.input_cad_vers, self.input_cad_id]
        for inp in cod_inputs:
            inp.textChanged.connect(lambda: self.cadastro_manager.print_cod_produto(cod_inputs))
        ##################################################################################################

        ##################################################################################################
        # EVENTOS TELA CONSULTA
        # Botões da tela Consulta
        self.btn_cons_buscar.clicked.connect(lambda: self.consulta_manager.to_query())
        self.btn_cons_limpar.clicked.connect(lambda: self.consulta_manager.clear_query_inputs())
        self.btn_cons_gerar_xlsx.clicked.connect(lambda: self.consulta_manager.generate_xlsx_from_query())
        self.btn_cons_limpar_table.clicked.connect(lambda: self.consulta_manager.clear_table())

        self.ck_filtrar_cod.stateChanged.connect(lambda: self.consulta_manager.ck_cons_cod_changer())

        # Variáveis da página Consulta
        self.today = dt.datetime.today()
        self.date_end.setDate(QDate(self.today.year, self.today.month, self.today.day))
        ##################################################################################################

        ##################################################################################################
        # EVENTOS TELA FAMILIAS
        # Botões da tela Familias
        self.btn_fam_criar.clicked.connect(lambda: self.familias_manager.criar_familia())
        self.btn_fam_editar.clicked.connect(lambda: self.familias_manager.editar_familias())
        self.btn_fam_atualizar.clicked.connect(lambda: self.familias_manager.query_familias())
        self.btn_fam_del.clicked.connect(lambda: self.familias_manager.deletar_familia())
        self.btn_fam_limpar.clicked.connect(lambda: self.familias_manager.limpar_inputs_edit())

        # Variáveis da página Famílias
        self.familias_manager.query_familias()
        ##################################################################################################
