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

    def _buscar_ativo(self, chave):
        # Recebe uma chave, e retorna o endereço do item ativo encontrado em uma tupla: (indice_do_bucket, indice_do_elemento)
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]
        
        if not bucket:
            return -1
        for elem in bucket:
            if elem[0] == chave and elem[1].estado:
                return (indice, bucket.index(elem))        

    def remover(self, chave):
        # Recebe uma chave, busca o endereço do elemento e altera seu status para "excluído"
        indices = self._buscar_ativo(chave)
        bucket = self.tabela[indices[0]] # Bucket dentro da tabela hash
        elem = bucket[indices[1]] # Elemento tupla (chave, valor)
        alvo = elem[1] # Objeto alvo, seja Funcionario ou Projeto
        alvo.estado = False
    
    def alterar(self, chave, valor):
        # Recebe um par chave - valor, busca o endereço do elemento e altera os dados no endereço encontrado
        pass
    
    def _funcao_hash(self, chave):
        # Recebe a chave, e retorna o índice da chave na tabela
        if isinstance(chave, str): # Chave seja string
            tamanho = self.tamanho
            chaveUnica = chave
            tamanhoLista = len(chaveUnica)
            Letra = list(chaveUnica)
            soma = 0
            
            for i in range(tamanhoLista):
                resultadoLetra = ord(Letra[i])
                soma = soma + resultadoLetra

            posiChave = soma % tamanho

            return posiChave

        elif isinstance(chave, int): # Caso seja int
            posiChave = chave % self.tamanho

            return posiChave

    def __str__(self):
        res = "tabela = [\n"
        for ind in range(self.tamanho):
            res += "    " + str(self.tabela[ind]) + ",\n"
        res += "]"
        
        return res

# Testes
func1 = Funcionario(123, "Alfredo", 15000)
func2 = Funcionario(452, "Junior", 50000)
func3 = Funcionario(3, "Julia", 2000)
proj1 = Projeto("Projetinhopae", "10/05/2032", "01/02/0332", 10, 10000, 123)
proj2 = Projeto("DeiaLinda", "10/05/2032", "01/02/0332", 2, 100000, 452)
proj3 = Projeto("SistemasDigitais", "10/05/2032", "01/02/0332", 5, 12000, 452)

tableFunc = TabelaHash()
tableFunc.inserir(func1)
tableFunc.inserir(func2)
tableFunc.inserir(func3)

tableProj = TabelaHash()
tableProj.inserir(proj1)
tableProj.inserir(proj2)
tableProj.inserir(proj3)

print(tableFunc)
print("\n\n")
print(tableProj)
