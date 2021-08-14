# Quantidade de testes
T = int(input())
# Estrutura de repetição
for i in range(0, T, 1):
    # Entrada de dados
    PA, PB, G1, G2 = [x for x in input().split()]
    # Transformação dos dados em inteiros em ponto flutuante
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float (G2)
    # Anos
    tempo = 0
    # Estrutura de repetição com 101 repetições máximas com condição de parada
    for i in range(0, 101, 1):
        # Condição de parada
        if PA>PB:
            # Imprime o resultado
            print("%s anos." %(tempo))
            # Para a estrutura de  repetição
            break
        # Soma o crescimento das populações
        PA += int(PA*(G1/100))
        PB += int(PB*(G2/100))
        # Soma 1 ano
        tempo += 1
    # Impressão do resultado se for mais de 1 século
    if tempo > 100:
        print("Mais de 1 seculo.")
