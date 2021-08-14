# Quantidade de teste
n = int(input())

# Variáveis necessárias para contagem
ratos = 0
sapos = 0
coelhos = 0
total = 0

# Estrutura de repetição com condições para contagem
for i in range(0, n, 1):
    # Entrada de dados
    quantia, tipo = input().split()
    quantia = int(quantia)
    # Total
    total += quantia
    # Condições para contagem
    if tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia
    else:
        coelhos += quantia

# Percentuais
percentual_ratos = round((ratos/total)*100, 2)
percentual_sapos = round((sapos/total)*100, 2)
percentual_coelhos = round((coelhos/total)*100, 2)

# Impressão de resultados
print("Total: %i cobaias" %total)
print("Total de coelhos: %i" %coelhos)
print("Total de ratos: %i" %ratos)
print("Total de sapos: %i" %sapos)
print("Percentual de coelhos: {0:.2f} %".format(percentual_coelhos))
print("Percentual de ratos: {0:.2f} %".format(percentual_ratos))
print("Percentual de sapos: {0:.2f} %".format(percentual_sapos))

