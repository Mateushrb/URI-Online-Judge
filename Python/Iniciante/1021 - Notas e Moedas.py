# Entrada de dados
valor = float(input())

# Cálculo com notas
notas_100 = int(valor//100) # Quantidade de notas de 100
valor = round(valor - (notas_100 * 100), 2) # Retira valor de notas de 100

notas_50 = int(valor//50) # Quantidade de notas de 50
valor = round(valor - (notas_50 * 50), 2) # Retira valor de notas de 50

notas_20 = int(valor//20) # Quantidade de notas de 20
valor = round(valor - (notas_20 * 20), 2) # Retira valor de notas de 20

notas_10 = int(valor//10) # Quantidade de notas de 10
valor = round(valor - (notas_10 * 10), 2) # Retira valor de notas de 10

notas_5 = int(valor//5) # Quantidade de notas de 5
valor = round(valor - (notas_5 * 5), 2) # Retira valor de notas de 5

notas_2 = int(valor//2) # Quantidade de notas de 2
valor = round(valor - (notas_2 * 2), 2) # Retira valor de notas de 2

# Cálculo com moedas
moeda_1_00 = int(valor//1) # Quantidade de moedas de 1.00
valor = round(valor - (moeda_1_00 * 1), 2) # Retira valor de moedas de 1 real

moeda_0_50 = int(valor//0.5) # Quantidade de moedas de 0.50
valor = round(valor - (moeda_0_50 * 0.5), 2) # Retira valor de moedas de 50 centavos

moeda_0_25 = int(valor//0.25) # Quantidade de moedas de 0.25
valor = round(valor - (moeda_0_25 * 0.25), 2) # Retira valor de moedas de 25 centavos

moeda_0_10 = int(valor//0.1) # Quantidade de moedas de 0.10
valor = round(valor - (moeda_0_10 * 0.1), 2) # Retira valor de moedas de 10 centavos

moeda_0_05 = int(valor//0.05) # Quantidade de moedas de 0.05
valor = round(valor - (moeda_0_05 * 0.05), 2) # Retira valor de moedas de 5 centavos

moeda_0_01 = valor * 100 # Quantidade de moedas de 0.01

# Saída de dados
print("NOTAS:")
print("%i nota(s) de R$ 100.00" %notas_100)
print("%i nota(s) de R$ 50.00" %notas_50)
print("%i nota(s) de R$ 20.00" %notas_20)
print("%i nota(s) de R$ 10.00" %notas_10)
print("%i nota(s) de R$ 5.00" %notas_5)
print("%i nota(s) de R$ 2.00" %notas_2)
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" %moeda_1_00)
print("%i moeda(s) de R$ 0.50" %moeda_0_50)
print("%i moeda(s) de R$ 0.25" %moeda_0_25)
print("%i moeda(s) de R$ 0.10" %moeda_0_10)
print("%i moeda(s) de R$ 0.05" %moeda_0_05)
print("%i moeda(s) de R$ 0.01" %moeda_0_01)
