# Entrada de dados
n = int(input())

# Estrutura de repetição com os parametros necessários
for i in range(1, n+1, 1):
    # Condição para calcular os divisores
    if n%i == 0:
        # Impressão do divisor encontrado
        print(i)
