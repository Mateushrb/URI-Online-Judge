# Estrutura de repetição
while True:
    # Entrada de dados
    x, y = [int(x) for x in input().split()]
    # Condição de parada
    if x == 0 or y == 0:
        break
    else: # Condições para execução do programa
        if x > 0:
            if y > 0:
                print("primeiro")
            else:
                print("quarto")
        else:
            if y > 0:
                print("segundo")
            else:
                print("terceiro")
