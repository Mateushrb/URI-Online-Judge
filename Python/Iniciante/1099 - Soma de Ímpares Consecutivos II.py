# Quantidade de teste
n = int(input())

# Estrutura de repetição
for i in range(0, n , 1):
    soma = 0
    x, y = [int(x) for x in input().split()]
    if x > y: # Condição se X for maior que Y
        if y%2 == 0: # Condição para deixar o valor de y entre os valores informados inicialmente
            y += 1
        else:
            y += 2
        while y < x: # Estrutura de repetição para somar os valores impares
            soma += y
            y += 2
        print(soma) # Impressão do resultado
    else: # Condição se Y for maior que X
        if x%2 == 0: # Condição para deixar o valor de x entre os valores informados inicialmente
            x += 1
        else:
            x += 2
        while x < y: # Estrutura de repetição para somar os valores impares
            soma += x
            x += 2
        print(soma) # Impressão do resultado
