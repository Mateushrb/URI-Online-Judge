# Variáveis necessárias para a soma
idade_somada = 0
qtd = 0

# Estrutura de repetição infinita com condição de parada
while True:
    # Entrada de dados
    individuos = int(input())
    # Condição para soma
    if individuos > 0:
        idade_somada += individuos
        qtd += 1
    # Condição de parada
    else:
        # Cálculo
        media = idade_somada / qtd
        break

# Impressão do resultado com fomatação
print("%0.2f" %(media))
