# Tipo de operação
operacao = str(input())
# Matriz
matriz = list()
# Criação da matriz
for i in range(0, 12, 1):
    linha = list()
    # Criação das linhas
    for l in range(0, 12, 1):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)
# Variáveis necessárias
soma = 0
divisor = 0
primeiro = 1
ultimo = 11
# Pegar valores solicitados
for i in range(0, 5, 1):
    for l in range(primeiro, ultimo, 1):
        soma += matriz[i][l]
        divisor += 1
    # Lógica para pegar os valores solicitados
    primeiro += 1
    ultimo -= 1

# Impressão do resultado
if operacao == 'S':
    soma = round(soma, 1)
    print('%0.1f' %(soma))
elif operacao == 'M':
    media = round(soma/divisor, 1)
    print('%0.1f' %(media))
else:
    pass
