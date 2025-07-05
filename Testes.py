from models.VetorLimitado import VetorLimitado
from models.Projeto import Projeto
from models.Funcionario import Funcionario

v = VetorLimitado(10)

f1 = Funcionario(10, "Ander2", 15000)
f2 = Funcionario(5, "Ander1", 15000)
f3 = Funcionario(15, "Ander3", 15000)

print(v)
v.append(f1)
print("\n")
print(v)
v.append(f2)
print("\n")
print(v)
v.append(f3)
print("\n")
print(v)