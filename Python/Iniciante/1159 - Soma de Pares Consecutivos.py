# Estrutura de repetição infinita com condição de parada
while True:
    # Entrada de dados
    x  = int(input())
    # Condição de parada
    if x == 0:
        break
    # Resultado
    resultado = 0
    # Estrutura com 5 repetições
    for i in range(0, 5, 1):
        # Condição de for par
        if x%2 == 0:
            # Soma o número par
            resultado += x
            # Soma mais 2 para o próximo número par consecutivo
            x += 2
        # Se for ímpar
        else:
            # Soma 1 pois o próximo é par
            x += 1
            # Soma o número par
            resultado += x
            # Soma mais 2 para o próximo número par consecutivo
            x += 2
    # Impressão do resultado
    print(resultado)
