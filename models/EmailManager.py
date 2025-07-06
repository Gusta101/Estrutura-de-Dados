from data import vetor_func, tabela_hash_email
from models.BuscasManager import BuscasManager
from textos import *


class EmailManager:
    def __init__(self):
        self.text = ""
        self.buscas_manager = BuscasManager()

    def menu(self):
        print(menu_email)
        escolha = input()
        match escolha:
            case "1":
                self.inserir_email()
            case "2":
                self.consulta_email()
            case "3":
                self.lista_emails()
            case "0":
                return
            case _:
                print(escolha_invalida)
        self.text = ""
        self.menu()

    # 1 - INSERIR EMAIL
    # Recebe a chave do funcionário e email, e insere na TabelaHash de Emails
    def inserir_email(self):
        func = self.recebe_funcionario()
        if not func:
            return
        email = input(insira_email)
        if tabela_hash_email.inserir(func.numero_funcional, email):
            print(f'Email {email} inserido para o funcionario {func.nome} | {func.numero_funcional} com sucesso')

    def recebe_funcionario(self):
        chave = int(input(insira_chave))
        vetor = vetor_func.vetor
        ind = self.buscas_manager.busca_binaria(chave, vetor, 0, len(vetor) - 1)
        if ind < 0:
            print(erro + "Funcionário não encontrado")
            return False
        return vetor[ind]

    # 2 - CONSULTA EMAIL
    # Consulta um email de uma chave funcionário específica
    def consulta_email(self):
        func = self.recebe_funcionario()
        if not func:
            return
        email = tabela_hash_email.buscar_item(func.numero_funcional)
        if not email:
            print(f'Funcionario {func.nome} nao encontrado na tabela emails')
            return
        print(f'Funcionario: {func.nome} | {func.numero_funcional}, Email: {email}')

    # 3 - LISTA EMAILS
    # Imprime uma lista de todos emails e suas chave funcionário
    def lista_emails(self):
        print(tabela_hash_email)
