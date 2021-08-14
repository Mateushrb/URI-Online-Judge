# Criação do vetor (lista)
vetor = list()
# Entrada do valor
x = int(input())
# Estrutura de repetição para o cálculo
for i in range(0, 10, 1):
    vetor.append(x)
    x *= 2
# Estrutura de repetição para impressão
for i in range(0, 10, 1):
    print("N[%s] = %s" %(i, vetor[i]))
