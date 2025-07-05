class VetorLimitado:
    def __init__(self, tamanho_max=10, vetor=[]):
        self.tamanho_max = tamanho_max
        self.vetor = vetor
    
    def append(self, dado):
        if len(self.vetor) < self.tamanho_max:
            self.vetor.append(dado)
            return 1
        return 0
