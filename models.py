class Funcionario:
    def __init__(self, numero_funcional, nome, salario):
        self.numero_funcional = numero_funcional
        self.nome = nome
        self.salario = salario
        self.estado = True
    
    def __str__(self):
        return f"=> Funcionário: {self.numero_funcional}; Nome: {self.nome}; Salario: {self.salario}; Estado: {self.estado}"
  

class Projeto:
    def __init__(self, nome, data_inicio, data_termino, tempo_estimado, valor_estimado, numero_func):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.tempo_estimado = tempo_estimado
        self.valor_estimado = valor_estimado
        self.numero_func = numero_func
        self.estado = True
    
    def __str__(self):
        return f"Projeto: {self.nome}"
 