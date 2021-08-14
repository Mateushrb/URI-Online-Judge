# Valor de entrada
n = int(input())

# Variáveis de soma
soma_in = 0
soma_out = 0

# Estrutura de repetição
for i in range(0, n, 1):
    valor = int(input())
    if valor >= 10 and valor <= 20:
        soma_in += 1
    else:
        soma_out += 1

# Saida de dados
print("%i in" %soma_in)
print("%i out" %soma_out)
