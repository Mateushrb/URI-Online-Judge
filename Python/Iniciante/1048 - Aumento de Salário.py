# Entrada
salario = float(input())

# Cálculo com saída embutida
if salario <= 400:
    reajuste = salario * 0.15
    novo_salario = salario + reajuste
    print("Novo salario: %0.2f" %novo_salario)
    print("Reajuste ganho: %0.2f" %reajuste)
    print("Em percentual: 15 %")
elif salario <= 800:
    reajuste = salario * 0.12
    novo_salario = salario + reajuste
    print("Novo salario: %0.2f" %novo_salario)
    print("Reajuste ganho: %0.2f" %reajuste)
    print("Em percentual: 12 %")
elif salario <= 1200:
    reajuste = salario * 0.1
    novo_salario = salario + reajuste
    print("Novo salario: %0.2f" %novo_salario)
    print("Reajuste ganho: %0.2f" %reajuste)
    print("Em percentual: 10 %")
elif salario <= 2000:
    reajuste = salario * 0.07
    novo_salario = salario + reajuste
    print("Novo salario: %0.2f" %novo_salario)
    print("Reajuste ganho: %0.2f" %reajuste)
    print("Em percentual: 7 %")
elif salario > 2000:
    reajuste = salario * 0.04
    novo_salario = salario + reajuste
    print("Novo salario: %0.2f" %novo_salario)
    print("Reajuste ganho: %0.2f" %reajuste)
    print("Em percentual: 4 %")
