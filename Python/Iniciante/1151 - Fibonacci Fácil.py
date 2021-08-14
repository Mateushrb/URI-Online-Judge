# Entrada de dados
n = int(input())

# Lista com os dois primeiros valores para iniciar os calculos
sequencia = [0, 1]

# Variáveis utilizadas nos cálculos
va = 0
fibo = 1

# Condição para o primeiro número
if n == 1:
    print(0)
# Condição para continuar a seguencia
else:
    # Estrutura de repetição
    for i in range(0, n-2, 1):
        # O novo número é ele mesmo mais o anterior
        fibo = fibo + va
        # O número anterior é o novo número menos o anterior
        va = fibo - va
        # Adicionar o novo número na lista
        sequencia.append(fibo)
    # Imprimir com asterísco para retirar os colchetes e virgulas
    print(*sequencia)
