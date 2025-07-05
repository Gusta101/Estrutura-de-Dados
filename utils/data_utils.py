from models.Funcionario import Funcionario
from models.Projeto import Projeto
from models.VetorLimitado import VetorLimitado

# Vetor de Funcionários
vetor_func = VetorLimitado(500)

# Vetor de Projetos
vetor_proj = VetorLimitado(2000)

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
    
    if vetor_func.append(projeto):
        return str(vetor_proj)
    else:
        return -1
