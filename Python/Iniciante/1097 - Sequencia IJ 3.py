# Variáveis necessárias
I = 1
J = 7

# Estruturas de repetição com saida
for i in range(0, 5, 1):
    for l in range(0, 3, 1):
        print("I=%i J=%i" %(I, J))
        J -= 1
    I += 2
    J += 5
