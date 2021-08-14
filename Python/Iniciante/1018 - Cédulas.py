# Entrada de dados
valor = int(input())

# Cálculo
notas_100 = valor//100 # Quantidade de notas de 100
valor = valor - (notas_100 * 100) # Novo valor

notas_50 = valor//50 # Quantidade de notas de 50
valor = valor - (notas_50 * 50) # Novo valor

notas_20 = valor//20 # Quantidade de notas de 20
valor = valor - (notas_20 * 20) # Novo valor

notas_10 = valor//10 # Quantidade de notas de 10
valor = valor - (notas_10 * 10) # Novo valor

notas_5 = valor//5 # Quantidade de notas de 5
valor = valor - (notas_5 * 5) # Novo valor

notas_2 = valor//2 # Quantidade de notas de 2
valor = valor - (notas_2 * 2) # Novo valor

notas_1 = valor//1 # Quantidade de notas de 1
valor = valor - (notas_1 * 1) # Novo valor

total = notas_100*100 + notas_50*50 + notas_20*20 + notas_10*10 + notas_5*5 + notas_2*2 + notas_1*1

# Saída de dados
print("%0.0f" %total)
print("%0.0f nota(s) de R$ 100,00" %notas_100)
print("%0.0f nota(s) de R$ 50,00" %notas_50)
print("%0.0f nota(s) de R$ 20,00" %notas_20)
print("%0.0f nota(s) de R$ 10,00" %notas_10)
print("%0.0f nota(s) de R$ 5,00" %notas_5)
print("%0.0f nota(s) de R$ 2,00" %notas_2)
print("%0.0f nota(s) de R$ 1,00" %notas_1)