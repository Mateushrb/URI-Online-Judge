# Quantidade de testes
n = int(input())
# Estrutura de repetição
for i in range(0, n, 1):
    # Número a ser testado
    x = int(input())
    # Variável para verificar se é primo
    primo = 0
    # Estrutura de repetição para testar se é primo
    for l in range(1, x+1, 1):
        # Verifica os divisores
        if x%l == 0:
            primo += 1
    # Imprime o resultado
    if primo == 2:
        print("%s eh primo" %(x))
    else:
        print("%s nao eh primo" %(x))
