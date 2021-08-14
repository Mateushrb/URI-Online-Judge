# Variáveis necessárias
media = 0 # Soma da média
n = 0 # Variávei para parar a estrutura de repetição

# Estrutura de repetição
while n != 2:
    nota = float(input()) # Entrada de dados
    # Condicação que verifica nota inválida
    if nota < 0 or nota > 10:
        print("nota invalida")
    else: # Condição para nota válida
        media += nota
        n += 1

# Impressão do resultado
print("media = {0:.2f}".format(media/2))
