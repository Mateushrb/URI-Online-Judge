# Valor de entrada
n = int(input())

multiplicador = 1
# Estrutura de repetição
for i in range(0, 10, 1):
    resultado = multiplicador * n
    print("%i x %i = %i" %(multiplicador, n, resultado))
    multiplicador += 1
