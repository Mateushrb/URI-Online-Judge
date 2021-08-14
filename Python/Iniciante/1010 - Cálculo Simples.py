# Entrada de dados
cod1, n_pecas1, valor1 = input().split()
cod2, n_pecas2, valor2 = input().split()

# Cálculo
valor_pagar = int(n_pecas1) * float(valor1) + int(n_pecas2) * float(valor2)

# Saída de dados
print("VALOR A PAGAR: R$ %0.2f" %valor_pagar)