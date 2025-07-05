class Funcionario:
    def __init__(self, numero_funcional, nome, salario):
        self.numero_funcional = numero_funcional
        self.nome = nome
        self.salario = salario
        self.estado = True
    
    def __str__(self):
        return f"=> Funcionário: {self.numero_funcional}; Nome: {self.nome}; Salario: {self.salario}; Estado: {self.estado}"
