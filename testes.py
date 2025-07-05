from models import Funcionario, Projeto
from query_utils import busca_funcionario, busca_funcionarios_bonus, busca_gerentes, busca_projetos_atraso, busca_projetos_prioridade
from TabelaHash import TabelaHash


# Testes

# TabelaHash
func1 = Funcionario(123, "Alfredo", 15000)
func2 = Funcionario(452, "Junior", 50000)
func3 = Funcionario(3, "Julia", 2000)
proj1 = Projeto("Projetinhopae", "10/05/2032", "01/02/0332", 10, 10000, 123)
proj2 = Projeto("Nasa", "10/05/2032", "01/02/0332", 2, 100000, 452)
proj3 = Projeto("SistemasDigitais", "10/05/2032", "01/02/0332", 5, 12000, 452)

tableFunc = TabelaHash()
tableFunc.inserir(func1)
tableFunc.inserir(func2)
tableFunc.inserir(func3)

tableProj = TabelaHash()
tableProj.inserir(proj1)
tableProj.inserir(proj2)
tableProj.inserir(proj3)

tableFunc.remover(123)

dados = {"nome": "Alexandre", "salario": 20000}
tableFunc.alterar(123, dados)

print(tableFunc.tabela[3][0][1])