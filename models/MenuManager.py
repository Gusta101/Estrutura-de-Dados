import os
import random

from models.BuscasManager import BuscasManager
from models.Funcionario import Funcionario
from models.Projeto import Projeto

from data import vetor_func, vetor_proj
from models.EmailManager import EmailManager
from textos import *

class MenuManager:
    def __init__(self):
        self.text = ""
        self.buscas_manager = BuscasManager()
        self.email_manager = EmailManager()

    # MENU PRINCIPAL
    def menu(self):
        print(menu)
        escolha = input()
        match escolha:
            case "1":
                self.listar_geral()
            case "2":
                self.adicionar_geral()
            case "3":
                self.edita_geral()
            case "4":
                self.remover_geral()
            case "5":
                self.buscas_manager.menu()
            case "6":
                self.email_manager.menu()
            case "0":
                return
            case _:
                print(escolha_invalida)
        self.text = ""
        self.menu()

    # 1 - LISTAGEM
    # Lista os vetores para facilitar a visualização
    def listar_geral(self):
        escolha = int(input(escolha_func_proj))
        if escolha == 1:
            print(vetor_func)
        elif escolha == 2:
            print(vetor_proj)
        elif escolha == 3:
            return
        else:
            print(escolha_invalida)
            self.listar_geral()

    # 2 - INSERÇÃO
    # Insere um funcionário ou projeto
    def adicionar_geral(self):
        escolha = int(input(escolha_func_proj))
        if escolha == 1: # Cria o objeto Funcionario e insere no vetor ordenado
            n_func = int(input(str_numero_func))
            if not n_func: n_func = random.randint(1, 500)
            nome_func = input(str_nome_func)
            salario_func = float(input(str_salario_func))
            func = Funcionario(n_func, nome_func, salario_func)
            if vetor_func.append(func):
                print(f'Funcionario {n_func} adicionado com sucesso')
            else:
                print(erro + f'Ja existe um funcionario com esse numero, ou a lista aingiu seu tamanho maximo')
        elif escolha == 2: # Cria o objeto Projeto e insere no vetor ordenado
            nome_proj = input(str_nome_proj)
            if not nome_proj: nome_proj = "Projeto " + str(random.randint(1, 2000))
            data_inicio = input(str_data_inicio)
            data_termino = input(str_data_termino)
            tempo_estimado = input(str_tempo_estimado)
            valor_estimado = input(str_valor_estimado)
            numero_func = input(str_numero_func_proj)
            proj = Projeto(nome_proj, data_inicio, data_termino, tempo_estimado, valor_estimado, numero_func)
            if vetor_proj.append(proj):
                print(f'Projeto {nome_proj} adicionado com sucesso')
            else:
                print(erro + f'Ja existe um projeto com esse nome, ou a lista aingiu seu tamanho maximo')
        elif escolha == 3:
            return
        else:
            print(escolha_invalida)
            self.adicionar_geral()

    # 3 - EDIÇÃO
    # Altera dados de um funcionário ou projeto pela chave
    def edita_geral(self):
        escolha = int(input(escolha_func_proj))
        if escolha == 1:
            print(vetor_func)
            chave = int(input(insira_chave + " (Número funcional)"))
            ind = vetor_func.buscar_item(chave)
            if ind < 0:
                print(chave_nao_encontrada)
                return
            func = vetor_func.vetor[ind]
            func.nome = input(str_nome_func)
            func.salario = float(input(str_salario_func))
            print("Dados alterados:\n" + func)
        elif escolha == 2:
            print(vetor_proj)
            chave = int(input(insira_chave + " (Nome do projeto)"))
            ind = vetor_proj.buscar_item(chave)
            if ind < 0:
                print(chave_nao_encontrada)
                return
            proj = vetor_proj.vetor[ind]
            proj.data_inicio = input(str_data_inicio)
            proj.data_termino = input(str_data_termino)
            proj.tempo_estimado = int(input(str_tempo_estimado))
            proj.valor_estimado = input(str_valor_estimado)
            proj.numero_func = int(input(str_numero_func_proj))
            print("Dados alterados:\n" + proj)
        elif escolha == 3:
            return
        else:
            print(escolha_invalida)
            self.listar_geral()

    # 4 - REMOCÃO
    # Altera o 'Estado' dos dados para False, evitando a perda de informação
    def remover_geral(self):
        escolha = int(input(escolha_func_proj))
        if escolha == 1:
            print(" - ".join([str(func.numero_funcional) for func in vetor_func.vetor if func.estado]))
            chave = int(input(insira_chave))
            if vetor_func.remover(chave):
                print(f'Funcionario {chave} removido com sucesso')
            else:
                print(chave_nao_encontrada)
        elif escolha == 2:
            print(" - ".join([proj.nome for proj in vetor_proj.vetor if proj.estado]))
            chave = input(insira_chave)
            if vetor_proj.remover(chave):
                print(f'Funcionario {chave} removido com sucesso')
            else:
                print(chave_nao_encontrada)
        elif escolha == 3:
            return
        else:
            print(escolha_invalida)
            self.listar_geral()

    # IMPRIME MENSAGENS NA TELA
    def print_text(self, text=""):
        os.system('cls')
        print(text + self.text)
