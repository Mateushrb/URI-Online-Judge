# Entrada de dados
h_inicial, h_final = [int(x) for x in input().split()]

# Cálculo
if h_inicial < h_final:
    duracao = h_final - h_inicial
else:
    duracao = 24 - h_inicial + h_final

# Saída de dados
print("O JOGO DUROU %i HORA(S)" %duracao)
