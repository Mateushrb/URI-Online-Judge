# Variável de condição para novos Grenais #
rep = 1

### Variáveis para elaboração da estatistica ###
grenais = 0
inter = 0
empates = 0
gremio = 0
###

while rep == 1: # Estrutura de repetição dos grenais
    
    # Quantidade de gols
    gols_inter, gols_gremio = [int(x) for x in input().split()]
    
    # Quantidade de Grenais
    grenais += 1
    
    # Condições
    if gols_inter > gols_gremio: # Condição para vitória do Inter
        inter += 1
    elif gols_inter == gols_gremio: # Condição para empate
        empates += 1
    else: # Condição para vitória do gremio
        gremio += 1
    
    print("Novo grenal (1-sim 2-nao)") # Pergunta para novo Grenal
    rep = int(input()) # Resposta da pergunta

# Impressão dos resultados
print("%s grenais" %(grenais))
print("Inter:%s" %(inter))
print("Gremio:%s" %(gremio))
print("Empates:%s" %(empates))

# Impressão do vencedor ou empate
if inter>gremio:
    print("Inter venceu mais")
elif inter == gremio:
    print("Nao houve vencedor")
else:
    print("Gremio venceu mais")
