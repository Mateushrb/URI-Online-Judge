# Quantidade de repetições
n = int(input())

# Estrutura de repetição
for i in range(0, n, 1):
    # Entrada de dados
    x, y = [int(x) for x in input().split()]
    # Condição para divisão impossível
    if y == 0:
        print("divisao impossivel")
    else:
        divisao = x / y
        divisao = round(divisao, 1)
        print(divisao)
