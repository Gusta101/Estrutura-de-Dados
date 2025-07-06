class Projeto:
    def __init__(self, nome, data_inicio, data_termino, tempo_estimado, valor_estimado, numero_func):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.tempo_estimado = tempo_estimado
        self.valor_estimado = valor_estimado
        self.numero_func = numero_func
        self.estado = True

    def get(self):
        return f"=> Projeto: {self.nome},DataInicio: {self.data_inicio}, DataTermino: {self.data_termino}, TempoEstimado: {self.tempo_estimado}, ValorEstimado: {self.valor_estimado}, Funcionario: {self.numero_func}, Estado: {"Ativo" if self.estado else "Inativo"}"
    
    def __str__(self):
        return f"=> Projeto: {self.nome}, Estado: {"Ativo" if self.estado else "Inativo"}"
