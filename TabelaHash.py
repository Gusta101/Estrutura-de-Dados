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
        # Recebe um par chave - valor, busca o endereço do elemento e insere os dados no endereço encontrado
        if isinstance(valor, Funcionario):
            chave = valor.numero_funcional
        elif isinstance(valor, Projeto):
            chave = valor.nome
        
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]
        
        if bucket:
            for elem in bucket:
                if elem[0] == chave and elem[1].estado:
                    return -1
        
        bucket.append((chave, valor)) # Valor deve ser o endereço do objeto, seja Funcionario ou Projeto

    def buscar(self, chave):
        # Recebe uma chave, retorna
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]
        
        if not bucket:
            return

    def remover(self, chave):
        # Recebe uma chave, busca o endereço do elemento e altera seu status para "excluído"
        pass
    
    def alterar(self, chave, valor):
        # Recebe um par chave - valor, busca o endereço do elemento e altera os dados no endereço encontrado
        pass
    
    def _funcao_hash(self, chave):
        # Recebe a chave, e retorna o índice da chave na tabela
        if isinstance(chave, str): # Chave seja string
            tamanho = self.tamanho
            chaveUnica = chave
            print(chaveUnica)
            tamanhoLista = len(chaveUnica)
            Letra = list(chaveUnica)
            soma = 0
            
            for i in range(tamanhoLista):
                resultadoLetra = ord(Letra[i])
                soma = soma + resultadoLetra

            posiChave = soma % tamanho
            tabela = [None] * tamanho
            tabela[posiChave] = soma

            return posiChave

        elif isinstance(chave,int):
            tamanho = self.tamanho
            chaveUnica = chave
            print(chaveUnica)
            tamanhoLista = len(chaveUnica)
            soma = 0
            
            for i in range(tamanhoLista):
                
                soma=soma+chaveUnica

            posiChave=soma%tamanho
            tabela = [None]*tamanho
            tabela[posiChave]=soma

            return posiChave




tebaleacsndkn = TabelaHash()
resultado = tebaleacsndkn._funcao_hash("Ana")
print(resultado)

