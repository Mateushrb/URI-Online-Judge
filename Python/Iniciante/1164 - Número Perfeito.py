# Quantidade de testes
n = int(input())
# estrutura de repetição
for i in range(0, n, 1):
    # Número para testar
    x = int(input())
    # Variável para verificar se é perfeito
    numero = 0
    # Estrutura de repetição para somar os divisores
    for i in range(1, x, 1):
        # Verifica se é divisor
        if x%i == 0:
            numero += i
    # Impressão do resultado
    if x == numero:
        print("%s eh perfeito" %(x))
    else:
        print("%s nao eh perfeito" %(x))
