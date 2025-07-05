from models import Funcionario, Projeto

class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho # Tamanho máx de Funcionarios = 500, e Projetos = 2000
        self.tabela = [[] for _ in range(tamanho)] # Cada lista dentro da tabela, é equivalente a um 'bucket'
        '''
        tabela = [ -> Tabela Hash
            [],
            [(chave1, valor1)], -> Bucket
            []
        ]
        '''
    
    def inserir(self, valor):
        # Recebe um objeto, busca o endereço hash da chave e insere os dados no primeiro endereço livre encontrado
        if isinstance(valor, Funcionario):
            chave = valor.numero_funcional
        elif isinstance(valor, Projeto):
            chave = valor.nome
        
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]
        
        if bucket:
            for elem in bucket:
                if elem[0] == chave and elem[1].estado: # Retorna erro caso a chave já exista na tabela
                    raise("Chave já existe na tabela")
        
        bucket.append((chave, valor)) # Valor deve ser o endereço do objeto, seja ele Funcionario ou Projeto

    def remover(self, chave):
        # Recebe uma chave, busca o endereço do elemento e altera seu status para "False"
        indices = self._buscar_ativo(chave)
        
        bucket = self.tabela[indices[0]] # Bucket dentro da tabela hash
        elem = bucket[indices[1]] # Elemento tupla (chave, valor)
        alvo = elem[1] # Objeto alvo
        alvo.estado = False
    
    def alterar(self, chave, valores: dict):
        # Recebe uma chave, e um dict valores com os dados que deseja alterar, busca o endereço do elemento e altera os dados no endereço encontrado
        indices = self._buscar_ativo(chave)
        
        if not indices:
            return -1
        
        alvo = self.tabela[indices[0]][indices[1]][1] # Seleciona o endereço de memória do objeto alvo
        
        for nome_atributo, valor_atributo in valores.items():
            if hasattr(alvo, nome_atributo): # Verifica se os atributos em 'valores', correspondem aos do objeto
                setattr(alvo, nome_atributo, valor_atributo) # Altera os dados do objeto, mantendo o seu ponteiro
    
    def _funcao_hash(self, chave):
        # Recebe a chave, e retorna o índice da chave na tabela
        if isinstance(chave, str): # Chave seja string
            soma = 0
            for letra in chave:
                soma += ord(letra)
            chave = soma
        
        return chave % self.tamanho

    def _buscar_ativo(self, chave):
        # Recebe uma chave, e retorna o endereço do item ativo encontrado, na forma de uma tupla: (indice_do_bucket_na_tabela, indice_do_elemento_no_bucket)
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]
        
        if not bucket:
            raise KeyError("Registro não encontrado")
        for elem in bucket:
            if elem[0] == chave and elem[1].estado:
                return (indice, bucket.index(elem))
        raise KeyError("O registro não existe ou foi excluído")      

    def __str__(self):
        return "tabela = [\n    " + ",\n    ".join(str(self.tabela[i]) for i in range(self.tamanho)) + "\n]"
