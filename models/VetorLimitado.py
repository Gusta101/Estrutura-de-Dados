from models.Funcionario import Funcionario
from models.Projeto import Projeto

class VetorLimitado:
    def __init__(self, tamanho_max=10, vetor:list=[]):
        self.tamanho_max = tamanho_max
        self.vetor = vetor
    
    # Adiciona dados ordenadamente no vetor. O tipo do dado deve ser informado (0 => Funcionario, 1 => Projeto)
    def append(self, dado):
        if len(self.vetor) < self.tamanho_max: # Encerra a função caso o tamanho máximo tenha sido atingido
            if len(self.vetor) <= 0: # Caso seja o primeiro valor apenas adiciona e encerra a função
                self.vetor.append(dado)
                return 1
            ind = 0
            
            if type(self.vetor[0]) == Funcionario.__class__:
                num = self.vetor[ind].numero_funcional
                while num < dado.numero_funcional:
                    ind += 1
                    num = self.vetor[ind].numero_funcional
                    
            if type(self.vetor[0]) == Projeto.__class__:
                nome = self.vetor[ind].nome
                while nome < dado.nome:
                    ind += 1
                    num = self.vetor[ind].nome
                    
            self.vetor.insert(ind, dado)
            return 1
        return 0
    
    def __str__(self):
        return "\n".join(str(item) for item in self.vetor)
