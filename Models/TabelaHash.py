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
        # Recebe um par chave - valor, busca o endereço do elemento e insere os dados no endereço encontrado
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]
        
        if bucket:
            for elem in bucket:
                if elem[0] == chave:
                    return -1
        
        bucket.append((chave, valor)) # Valor deve ser o endereço do objeto, seja Funcionario ou Projeto

    def remover(self, chave):
        # Recebe uma chave, busca o endereço do elemento e altera seu status para "excluído"
        pass
    
    def alterar(self, chave, valor):
        # Recebe um par chave - valor, busca o endereço do elemento e altera os dados no endereço encontrado
        pass
    
    def _funcao_hash(self, chave):
        # Recebe a chave, seja str ou int, e retorna o endereço da chave na tabela
        
        tamanho = self.tamanho
        chaveUnica = chave
        print(chaveUnica)
        tamanhoLista = len(chaveUnica)
        Letra = list(chaveUnica)
        soma=0
       
        for i in range(tamanhoLista):
            resultadoLetra = ord(Letra[i])
            soma=soma+resultadoLetra

        posiChave=soma%tamanho
        tabela = [None]*tamanho
        tabela[posiChave]=soma

        return posiChave


table1 = TabelaHash(13)
tebaleacsndkn = TabelaHash(500)

print(table1)