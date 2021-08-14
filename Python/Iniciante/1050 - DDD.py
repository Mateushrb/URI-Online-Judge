# Leitura do código DDD
DDD = int(input())

# Dicionário
codigos = {61:'Brasilia', 71:'Salvador', 11:'Sao Paulo', 21:'Rio de Janeiro', 32:'Juiz de Fora', 19:'Campinas', 27:'Vitoria', 31:'Belo Horizonte'}

# Seleção com saída de dados
if DDD not in codigos:
    print("DDD nao cadastrado")
else:
    cidade = codigos[DDD]
    print(cidade)
