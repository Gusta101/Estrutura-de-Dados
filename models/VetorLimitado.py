from models.Funcionario import Funcionario
from models.Projeto import Projeto


class VetorLimitado:
    def __init__(self, tamanho_max=10, vetor=None):
        self.tamanho_max = tamanho_max
        self.vetor = vetor if vetor is not None else []

    # Adiciona dados ordenadamente no vetor. O tipo do dado deve ser informado (0 => Funcionario, 1 => Projeto)
    def append(self, dado):
        tamanho = len(self.vetor)
        if tamanho < self.tamanho_max: # Encerra a função caso o tamanho máximo tenha sido atingido
            if tamanho <= 0: # Caso seja o primeiro valor apenas adiciona e encerra a função
                self.vetor.append(dado)
                return 1
            ind = tamanho

            if isinstance(self.vetor[0], Funcionario):
                for i in range(tamanho):
                    if dado.numero_funcional <= self.vetor[i].numero_funcional:
                        if dado.numero_funcional == self.vetor[i].numero_funcional:
                            return 0
                        ind = i
                        break

            if isinstance(self.vetor[0], Projeto):
                for i in range(tamanho):
                    if dado.nome <= self.vetor[i].nome:
                        if dado.nome == self.vetor[i].nome:
                            return 0
                        ind = i
                        break

            self.vetor.insert(ind, dado)
            return 1
        return 0

    # Busca uma chave no vetor e retorna o índice do item correspondente
    def buscar_item(self, chave):
        tamanho = len(self.vetor)
        if tamanho == 0:
            return -1
        for i in range(tamanho):
            if isinstance(self.vetor[0], Funcionario) and chave == self.vetor[i].numero_funcional:
                return i
            if isinstance(self.vetor[0], Projeto) and chave == self.vetor[i].nome:
                return i
        return -1

    # Altera o valor 'Estado' de um dado conforme sua chave
    def remover(self, chave):
        indice = self.buscar_item(chave)
        if indice >= 0:
            self.vetor[indice].estado = False
            return 1
        return 0

    def __str__(self):
        return "\n".join(str(item) for item in self.vetor)
