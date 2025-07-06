from data import vetor_func, vetor_proj
from textos import *


class BuscasManager:
    def __init__(self):
        self.text = ""

    # MENU DE BUSCAS
    def menu(self):
        print(menu_buscas)
        escolha = input()
        match escolha:
            case "1":
                self.busca_funcionario()
            case "2":
                self.busca_por_salario()
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                return
            case _:
                print(escolha_invalida)
        self.text = ""
        self.menu()

    # 1 - BUSCA FUNCIONÁRIO
    # Retorna os dados de um funcionário, de acordo com a chave fornecida
    def busca_funcionario(self):
        chave = int(input(insira_chave))
        vetor = vetor_func.vetor
        ind = self.busca_binaria(chave, vetor, 0, len(vetor) - 1)
        if ind >= 0:
            print("Encontrado!\n" + str(vetor[ind]))
        else:
            print(erro + "Não foi possível encontrar essa chave")

    def busca_binaria(self, chave, vetor, primeiro, ultimo):
        if primeiro > ultimo:
            return -1
        meio = (ultimo + primeiro) // 2
        valor = vetor[meio].numero_funcional
        if valor == chave:
            return meio
        if chave < valor:
            return self.busca_binaria(chave, vetor, primeiro, meio - 1)
        if chave > valor:
            return self.busca_binaria(chave, vetor, meio + 1, ultimo)

    # 2 - BUSCA POR SALARIO
    # Retorna uma lista ordenada decrescentemente com Merge Sort, de funcionários com salário maior que 10.000
    def busca_por_salario(self):
        lista = [func for func in vetor_func.vetor if func.salario > 10000]
        self.merge_sort_dec(lista)
        for i in lista:
            print(i)

    def merge_sort_dec(self, vetor):
        if len(vetor) > 1:
            meio = len(vetor) // 2
            esquerda = vetor[:meio]
            direita = vetor[meio:]

            self.merge_sort_dec(esquerda)
            self.merge_sort_dec(direita)

            i = j = k = 0

            while i < len(esquerda) and j < len(direita):
                if esquerda[i].salario > direita[j].salario:
                    vetor[k] = esquerda[i]
                    i += 1
                else:
                    vetor[k] = direita[j]
                    j += 1
                k += 1

            while i < len(esquerda):
                vetor[k] = esquerda[i]
                k += 1
                i += 1

            while j < len(direita):
                vetor[k] = direita[j]
                j += 1
                k += 1

    # 3 - BUSCA PROJETOS GRANDES
    #
