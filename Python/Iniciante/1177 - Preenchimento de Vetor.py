# Entrada
T = int(input())
N = []

# Iniciar a lista
for i in range(0, T, 1):
    N.append(i)

valor = 0

# Adicionar os valores restantes
for l in range(0, 1000-T, 1):
    # Condição para repetir os valores
    if valor == T:
        valor = 0
    N.append(valor)
    valor += 1

# Estrutura de repetição para impressão dos resultados
for m in range(0, len(N), 1):
    print("N[%s] = %s" %(m, N[m]))
