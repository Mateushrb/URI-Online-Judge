# Entrada de dados
salario = float(input())

# Cálculo
if salario < 2000.00:
    print("Isento")
elif salario <= 3000.00:
    salario -= 2000
    salario *= 0.08 # Imposto 8%
    print("R$ %0.2f" %salario)
elif salario <= 4500.00:
    salario -= 2000
    imposto8 = 1000*0.08 # Imposto 8%
    salario -= 1000
    salario *= 0.18 # Imposto 18%
    salario += imposto8
    print("R$ %0.2f" %salario)
elif salario > 4500.00:
    salario -= 2000
    imposto8 = 1000*0.08 # Imposto 8%
    salario -= 1000
    imposto18 = 1500*0.18 # Imposto 18%
    salario -= 1500
    salario *= 0.28 # Imposto 28%
    salario += imposto8
    salario += imposto18
    print("R$ %0.2f" %salario)
