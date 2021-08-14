# Estrutura de repetição com condição de parada
while True:
    # Entrada de dados
    x, y = [int(x) for x in input().split()]
    if x == y: # Condição de parada
        break
    else: # Condições para impressão do resultado
        if x > y:
            print("Decrescente")
        else:
            print("Crescente")
