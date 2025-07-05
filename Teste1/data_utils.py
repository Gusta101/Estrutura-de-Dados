from models.Funcionario import Funcionario
from models.Projeto import Projeto
from models.VetorLimitado import VetorLimitado

from data import vetor_proj
from data import vetor_func


# INSERÇÃO
# Insere funcionário no vetor principal "vetor_func"
def inserir_funcionario(dados: list):
    nome = dados[0]
    numero_funcional = dados[1]
    salario = dados[2]
    funcionario = Funcionario(nome=nome, numero_funcional=numero_funcional, salario=salario)
    
    if vetor_func.append(funcionario):
        return str(vetor_func)
    else:
        return -1

# Insere projeto no vetor principal "vetor_proj"
def inserir_projeto(dados: list):
    nome = dados[0]
    tempo_estimado = dados[1]
    valor_estimado = dados[2]
    n_funcionario = dados[3]
    data_inicio = dados[4]
    data_termino = dados[5]
    projeto = Projeto(nome=nome, data_inicio=data_inicio, data_termino=data_termino, tempo_estimado=tempo_estimado, valor_estimado=valor_estimado, numero_func=n_funcionario)
    
    if vetor_proj.append(projeto):
        return str(vetor_proj)
    else:
        return -1


# REMOÇÃO
# Remove funcionario
def remover_funcionario(chave):
    return vetor_func.remover(chave)

# Remove projeto
def remover_projeto(chave):
    return vetor_proj.remover(chave)

# AUXILIARES
# Retorna uma lista de números de funcionários ativos do vetor_func
def get_numeros_func_ativos():
    return [str(func.numero_funcional) for func in vetor_func.vetor if func.estado]

# Retorna uma lista de nomes de projetos ativos do vetor_proj
def get_nomes_proj_ativos():
    return [proj.nome for proj in vetor_proj.vetor if proj.estado]
