# Tipo de operação
operacao = str(input())
# Estrutura de repetição com entrada de dados para criação da matriz
matriz = list()
for i in range(0, 12, 1):
    linha = list()
    for l in range(0, 12, 1):
        elemento = float(input())
        linha.append(elemento)
    matriz.append(linha)
# Variáveis necessárias
primeiro = 5
ultimo = 6
soma = 0
divisor = 0
# Estrutura de repetição para pegar os números solicitados
for i in range(7, 12, 1):
    for l in range(primeiro, ultimo+1, 1):
        soma += matriz[i][l]
        divisor += 1
    primeiro -= 1
    ultimo += 1
# Impressão do resultado
if operacao == 'S':
    soma = round(soma, 1)
    print('%1.1f' %(soma))
elif operacao == 'M':
    media = soma/divisor
    round(media, 1)
    print('%1.1f' %(media))
else:
    pass
