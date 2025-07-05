class Funcionario:
    def __init__(self, numero_funcional, nome, salario):
        self.numero_funcional = int(numero_funcional)
        self.nome = nome
        self.salario = float(salario)
        self.estado = True
    
    def __str__(self):
        return f"=> Funcionário: {self.numero_funcional}; Nome: {self.nome}; Salario: {self.salario}; Estado: {self.estado}"
