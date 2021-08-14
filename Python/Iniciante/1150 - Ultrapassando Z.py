# Valor de "x" e primeiro valor de "z"
x = int(input())
z = int(input())

# Estrutura de repetição para pegar um valor de z maior que x
while z <= x:
    z = int(input())

# Variáveis necessárias para soma e contagem
contador = 1
soma = x

# Estrutura de repetição para soma e contagem
while soma < z:
    soma += x + 1
    x += 1
    contador += 1

# Resultado
print(contador)
