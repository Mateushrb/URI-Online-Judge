# Entrada do número que será calculado
n = int(input())

# Variável que armazenará o cálculo
fatorial = 1

# Estrutura de repetição para realizar o cálculo
for i in range(0, n, 1):
    # A lógica é declarar a variável "fatorial" como 1
    # usar "*=" para multiplicar a variável com o que
    # é declarado para ela, i começa em 0, por isso é
    # necessário somar 1, a partir disso a própria
    # estrutura de repetição vai aumentando de 1 em 1
    # e valor de i e "*=" vai multiplicando até chegar
    # ao resultado final
    fatorial *= (i+1)

# Impressão do resultado
print(fatorial)
