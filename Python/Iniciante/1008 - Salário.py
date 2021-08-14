# Entrada de dados
numero = int(input())
n_horas = int(input())
valor = float(input())

# Cálculo
salario = n_horas * valor

# Saída de dados
print("NUMBER = {0}".format(numero))
print("SALARY = U$ %0.2f" %salario)