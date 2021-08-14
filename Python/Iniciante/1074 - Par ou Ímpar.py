# Valor de entrada
n = int(input())

# Estrutura de repetição
for i in range(0, n, 1):
    valor = int(input())
    r = ''
    # Condições com saída de dados
    if valor == 0:
        print("NULL")
    else:
        if valor%2 == 0:
            r += 'EVEN '
        else:
            r += 'ODD '
        if valor < 0:
            r += 'NEGATIVE'
        else:
            r += 'POSITIVE'
        print(r)
