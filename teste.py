import random

from models.BuscasManager import BuscasManager
from models.Funcionario import Funcionario
from models.VetorLimitado import VetorLimitado

bm = BuscasManager()

nomes_base = [
    "Ander", "Bruna", "Carlos", "Daniela", "Eduardo", "Fernanda",
    "Gustavo", "Helena", "Igor", "Julia", "Karla", "Lucas", "Marcos",
    "Nina", "Otavio", "Patricia", "Rafael", "Sabrina", "Thiago", "Vanessa"
]

funcionarios = VetorLimitado(200)

for i in range(1, 101):  # 100 funcionários
    nome = random.choice(nomes_base) + str(i)
    salario = random.randint(500, 20000)  # Salários entre R$500 e R$20.000
    f = Funcionario(i, nome, salario)
    funcionarios.append(f)

bm.merge_sort_dec(funcionarios.vetor)

print(funcionarios)