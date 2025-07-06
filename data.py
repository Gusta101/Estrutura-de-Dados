from models.TabelaHash import TabelaHash
from models.VetorLimitado import VetorLimitado
from models.Funcionario import Funcionario
from models.Projeto import Projeto

f1 = Funcionario(15, "Ana Beatriz Costa", 16500)   # Responsável por p1 e p5
f2 = Funcionario(88, "Lucas Almeida", 8800)        # Responsável por p6 e p8
f3 = Funcionario(150, "Mariana Lima", 22000)       # Responsável por p7 e p11
f4 = Funcionario(212, "Rafael Oliveira", 19500)    # Responsável por p9 e p15
f5 = Funcionario(42, "Juliana Pereira", 9500)      # Responsável por p13 e p20
f6 = Funcionario(301, "Bruno Martins", 14000)      # Responsável por p16
f7 = Funcionario(45, "Camila Ferreira", 7200)      # Responsável por p3
f8 = Funcionario(450, "Fernando Souza", 25000)     # Responsável por p14
f9 = Funcionario(10, "Patrícia Gomes", 8500)
f10 = Funcionario(50, "Ricardo Azevedo", 11500)
f11 = Funcionario(99, "Sofia Ribeiro", 6800)
f12 = Funcionario(101, "Daniel Rocha", 10500)
f13 = Funcionario(250, "Laura Barbosa", 28000)
f14 = Funcionario(499, "Thiago Santos", 9900)

p1 = Projeto('Rebranding Corporativo', '10/01/2024', '10/04/2024', 3, 45000, 15)
p2 = Projeto('Desenvolvimento Web Básico', '01/01/2024', '30/06/2024', 6, 120000, 221)
p3 = Projeto('Pesquisa de Mercado Global', '01/05/2024', '30/06/2024', 2, 30000, 45)
p4 = Projeto('Expansão Internacional - Fase 1', '01/08/2024', '01/01/2025', 5, 250000, 310)
p5 = Projeto('Otimização de SEO', '01/02/2025', '01/06/2025', 4, 65000, 15)
p6 = Projeto('Hotfix de Segurança Urgente', '01/07/2025', '05/07/2025', 1, 1500000, 88)
p7 = Projeto('Construção do Data Warehouse', '01/11/2024', None, 12, 480000, 150)
p8 = Projeto('Desenvolvimento App Mobile "ConectaVocê"', '15/01/2025', None, 9, 180000, 88)
p9 = Projeto('Migração para Cloud Híbrida', '01/03/2025', None, 18, 3200000, 212)
p10 = Projeto('Implementação de Sistema ERP SAP', '01/02/2025', '01/07/2026', 18, 1200000, 410)
p11 = Projeto('Pesquisa e Desenvolvimento de IA Generativa', '01/06/2025', None, 24, 750000, 150)
p12 = Projeto('Sistema de Gestão de Clientes (CRM)', '15/05/2024', '15/12/2024', 7, 190000, 25)
p13 = Projeto('Criação de Landing Pages de Marketing', '10/01/2025', '10/03/2025', 2, 25000, 42)
p14 = Projeto('Automação de Linha de Produção', '01/03/2024', '01/05/2025', 55, 850000, 450)
p15 = Projeto('Painel de Controle de Logística', '20/09/2024', '20/02/2025', 5, 95000, 212)
p16 = Projeto('Desenvolvimento Plataforma E-commerce', '15/02/2023', '15/01/2024', 11, 580000, 301)
p17 = Projeto('Análise de Big Data para Varejo', '01/04/2025', None, 10, 280000, 345)
p18 = Projeto('Digitalização de Arquivo Histórico', '01/01/2023', None, 10, 650000, 112)
p19 = Projeto('Manutenção de Servidores Legados', '01/07/2024', None, 12, 40000, 199)
p20 = Projeto('Integração de API de Pagamentos', '15/06/2025', None, 3, 70000, 42)

email1 = "teste15@gmail.com"
email2 = "teste42@gmail.com"
email3 = "teste212@gmail.com"
email4 = "teste88@gmail.com"

vetor_func = VetorLimitado(500)

vetor_proj = VetorLimitado(2000)

tabela_hash_email = TabelaHash(500)

vetor_func.append(f1)
vetor_func.append(f2)
vetor_func.append(f3)
vetor_func.append(f4)
vetor_func.append(f5)
vetor_func.append(f6)
vetor_func.append(f7)
vetor_func.append(f8)
vetor_func.append(f9)
vetor_func.append(f10)
vetor_func.append(f11)
vetor_func.append(f12)
vetor_func.append(f13)
vetor_func.append(f14)

vetor_proj.append(p1)
vetor_proj.append(p2)
vetor_proj.append(p3)
vetor_proj.append(p4)
vetor_proj.append(p5)
vetor_proj.append(p6)
vetor_proj.append(p7)
vetor_proj.append(p8)
vetor_proj.append(p9)
vetor_proj.append(p10)
vetor_proj.append(p11)
vetor_proj.append(p12)
vetor_proj.append(p13)
vetor_proj.append(p14)
vetor_proj.append(p15)
vetor_proj.append(p16)
vetor_proj.append(p17)
vetor_proj.append(p18)
vetor_proj.append(p19)
vetor_proj.append(p20)

tabela_hash_email.inserir(15, email1)
tabela_hash_email.inserir(42, email2)
tabela_hash_email.inserir(212, email3)
tabela_hash_email.inserir(88, email4)
