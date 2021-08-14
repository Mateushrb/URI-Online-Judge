# Entrada de dados
tempo = int(input())

# Cálculo
horas = tempo//3600
tempo = tempo - (horas * 3600) # Novo tempo

minutos = tempo//60
segundos = tempo - (minutos * 60)

# Saída de dados
print("{0}:{1}:{2}".format(horas, minutos, segundos))