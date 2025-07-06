from data import vetor_proj

erro = "Erro: "

menu = """
    1 - Listar Funcionários ou Projetos
    2 - Adicionar Funcionário ou Projeto
    3 - Editar um Funcionário ou Projeto
    4 - Remover um Funcionário ou Projeto
    5 - Realizar Buscas
    6 - Gerenciar emails de gerentes
    0 - Encerrar aplicação
"""

menu_buscas = """
    1 - Funcionário a partir do número funcional
    2 - Salários maiores que 10.000 reais (Decrescente)
    3 - Projetos em andamento e maiores que 500.000 reais (Crescente)
    4 - Projetos atrasados (Em andamento ou não, ordenados pelo atraso)
    5 - Funcionarios com projetos em andamento atribuidos (Ordem alfabetica)
    0 - Voltar
"""

menu_email = """
    1 - Inserir email
    2 - Consultar email
    3 - Consultar todos emails
    0 - Voltar
"""

escolha_func_proj = """
    Funcionario ou Projeto?
    1 - Funcionario
    2 - Projeto
    3 - Voltar
"""

escolha_invalida = "Escolha invalida, escolha novamente:\n"
insira_chave = "Insira a chave de identificacao: "
insira_email = "Insira o email: "

chave_nao_encontrada = "Chave não encontrada, tente novamente"

str_numero_func = "Número funcional do Funcionario (unico): "
str_nome_func = "Nome do Funcionario: "
str_salario_func = "Salario do Funcionario: "

str_nome_proj = "Nome do projeto (unico): "
str_data_inicio = "Data de inicio 'DD/MM/AAAA' : "
str_data_termino = "Data de termino 'DD/MM/AAAA' (Deixe vazio se estiver em andamento): "
str_tempo_estimado = "Tempo estimado em meses: "
str_valor_estimado = "Valor estimado: "
str_numero_func_proj = "Numero do funcionario responsavel: "
