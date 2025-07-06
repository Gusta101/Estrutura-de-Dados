import calendar
from datetime import datetime, date

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
                self.busca_projetos_grandes()
            case "4":
                self.busca_projetos_atrasados()
            case "5":
                self.busca_gerentes()
            case "0":
                return
            case _:
                print(escolha_invalida)
        self.text = ""
        self.menu()

    # 1 - BUSCA FUNCIONÁRIO
    # Imprime os dados de um funcionário, de acordo com a chave fornecida
    def busca_funcionario(self):
        chave = int(input(insira_chave))
        vetor = vetor_func.vetor
        ind = self.busca_binaria(chave, vetor, 0, len(vetor) - 1)
        if ind >= 0:
            if vetor[ind].estado:
                print("Encontrado!\n" + str(vetor[ind]))
            else:
                print(erro + "O funcionário encontrado foi desligado")
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
    # Imprime uma lista ordenada decrescentemente com Merge Sort, de funcionários com salário maior que 10.000
    def busca_por_salario(self):
        lista = [func for func in vetor_func.vetor if func.salario > 10000]
        self.merge_sort_dec(lista)
        for i in lista:
            print(f'Funcionario: {i.nome}, Salario: {i.salario}')

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
    # Imprime uma lista de projetos sem data de término (em andamento), com valor maior que 500.000, em ordem crescente
    def busca_projetos_grandes(self):
        lista = [proj for proj in vetor_proj.vetor if proj.valor_estimado > 500000 and not proj.data_termino]
        self.heap_sort(lista)
        for i in lista:
            print(str(i) + f', Valor estimado: {i.valor_estimado}')

    def heapify(self, vetor, tamanho, i):
        maior = i
        f1 = i * 2 + 1
        f2 = i * 2 + 2
        if f1 < tamanho and vetor[maior].valor_estimado < vetor[f1].valor_estimado:
            maior = f1
        if f2 < tamanho and vetor[maior].valor_estimado < vetor[f2].valor_estimado:
            maior = f2
        if maior != i:
            vetor[i], vetor[maior] = vetor[maior], vetor[i]
            self.heapify(vetor, tamanho, maior)

    def heap_sort(self, vetor): # ordem de valor, heap sort
        tamanho = len(vetor)
        for i in range(tamanho // 2 - 1, -1, -1):
            self.heapify(vetor, tamanho, i)
        for i in range(tamanho - 1, 0, -1):
            vetor[i], vetor[0] = vetor[0], vetor[i]
            self.heapify(vetor, i, 0)

    # 4 - BUSCA PROJETOS COM ATRASO
    # Imprime uma lista de projetos, em andamento ou não, que passaram do prazo previsto, ordenados pelo tempo de atraso
    def busca_projetos_atrasados(self): # ordenar com o algoritmo livre, e listar se está em andamento ou não
        lista_atrasados = self.filtra_projetos_atrasados(vetor_proj.vetor)

        for i in range(1, len(lista_atrasados)): # Insertion Sort com Tuplas
            chave = lista_atrasados[i]
            j = i - 1
            while j >= 0 and chave[1] < lista_atrasados[j][1]:
                lista_atrasados[j + 1] = lista_atrasados[j]
                j -= 1
            lista_atrasados[j + 1] = chave

        for proj, atraso in lista_atrasados:
            print(f'Projeto: {proj.nome}, {'Em andamento' if proj.estado else 'Encerrado'}, Tempo de atraso (em meses): {str(atraso)}')

    def filtra_projetos_atrasados(self, vetor):
        lista_atrasados = []
        hoje = date.today()
        for proj in vetor:
            data_inicio = datetime.strptime(proj.data_inicio, "%d/%m/%Y").date()
            data_prevista = self.calcular_data_prevista(data_inicio, int(proj.tempo_estimado))
            esta_atrasado = False
            atraso = 0
            if proj.data_termino is None:
                if hoje > data_prevista:
                    esta_atrasado = True
                    atraso = self.calcular_atraso(hoje, data_prevista)
            else:
                data_termino = datetime.strptime(proj.data_termino, "%d/%m/%Y").date()
                if data_termino > data_prevista:
                    esta_atrasado = True
                    atraso = self.calcular_atraso(data_termino, data_prevista)
            if esta_atrasado:
                lista_atrasados.append((proj, atraso))
        return lista_atrasados

    def calcular_atraso(self, data_fim, data_inicio):
        if data_fim < data_inicio:
            return 0
        meses = (data_fim.year - data_inicio.year) * 12 + (data_fim.month - data_inicio.month)
        if data_fim.day < data_inicio.day:
            meses -= 1
        return meses

    def calcular_data_prevista(self, data, meses):
        novo_ano = data.year + (data.month + meses - 1) // 12
        novo_mes = (data.month + meses - 1) % 12 + 1
        ultimo_dia_do_mes_destino = calendar.monthrange(novo_ano, novo_mes)[1]
        novo_dia = min(data.day, ultimo_dia_do_mes_destino)
        return date(novo_ano, novo_mes, novo_dia)

    # 5 - BUSCA GERENTES
    # Imprime, ordem alfabética, os funcionários responsáveis por projetos em andamento
    def busca_gerentes(self): # busca o mais otimizada o possível
        projetos_em_andamento = [proj for proj in vetor_proj.vetor if proj.estado]
        nums_func = []
        for proj in projetos_em_andamento:
            if proj.numero_func not in nums_func:
                nums_func.append(proj.numero_func)
        func_validos = []
        vetor = vetor_func.vetor
        for num in nums_func:
            ind = self.busca_binaria(num, vetor, 0, len(vetor) - 1)
            if ind > -1:
                func_validos.append(vetor[ind])

        for i in range(1, len(func_validos)):  # Insertion Sort dos Funcionários, pelo Nome
            chave = func_validos[i]
            j = i - 1
            while j >= 0 and chave.nome < func_validos[j].nome:
                func_validos[j + 1] = func_validos[j]
                j -= 1
            func_validos[j + 1] = chave

        for f in func_validos:
            print(f)
