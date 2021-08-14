# Entrada de dados
nome = input()
salario_fixo = float(input())
total_vendas = float(input())

# Cálculo
total = salario_fixo + total_vendas * 0.15

# Saida de dados
print("TOTAL = R$ %0.2f" %total)