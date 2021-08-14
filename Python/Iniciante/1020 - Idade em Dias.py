# Entrada de dados
idade_em_dias = int(input())

# Cálculo
anos = idade_em_dias//365
idade_em_dias = idade_em_dias - (anos * 365) # Desconto de anos

meses = idade_em_dias//30
dias = idade_em_dias - (meses * 30) # Desconto de meses, sobra os dias

# Saída de dados
print("%s ano(s)" %anos)
print("%s mes(es)" %meses)
print("%s dia(s)" %dias)