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
    
    def inserir(self, chave, valor):
        # Recebe um objeto e chave, busca o endereço hash da chave e insere os dados no primeiro endereço livre encontrado
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]
        
        if bucket:
            for elem in bucket:
                if elem[0] == chave: # Retorna erro caso a chave já exista na tabela
                    print("Chave já existe na tabela de emails")
                    return 0
        
        bucket.append((chave, valor)) # Valor deve ser o endereço do objeto, seja ele Funcionario ou Projeto
        return 1
    
    def _funcao_hash(self, chave):
        # Recebe a chave, e retorna o índice da chave na tabela
        return chave % self.tamanho

    def buscar_item(self, chave):
        # Recebe uma chave, e retorna o valor do item ativo encontrado, na forma de uma tupla: (indice_do_bucket_na_tabela, indice_do_elemento_no_bucket)
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]
        
        if not bucket:
            print("Registro não encontrado")
            return 0
        for elem in bucket:
            if elem[0] == chave:
                return elem[1]
        print("O registro não existe ou foi excluído")
        return 0

    def __str__(self):
        return "tabela = [\n    " + ",\n    ".join(str(self.tabela[i]) for i in range(self.tamanho) if self.tabela[i]) + "\n]"
