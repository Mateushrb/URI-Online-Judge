# Quantidade de casos de teste
n = int(input())

# Estrutura de repetição na qual "n" é a
# quantidade de repetições
for i in range(0, n, 1):
    # Entrada dos números para o teste
    x, y = [int(x) for x in input().split()]
    # Variável "soma" para somar os números
    # e obter o resultado final
    soma = 0
    # Estrutura de repetição com condição de parada apenas
    # quando encontrar a quantidade de ímpares informados
    while y != 0:
        # Estrutura de condição para testar se o número é par
        if x%2 == 0:
            # Caso afirmativo, soma 1 para testa o próximo número
            x += 1
        # Se o número for ímpar
        else:
            # Soma com o número atual da variável "soma"
            soma += x
            # Soma 1 na variável "x" para testar o próximo número
            x += 1
            # Subtrai 1 da variável "y" que é a quantidade de teste
            y -= 1
    # Imprime o resultado final
    print(soma)
