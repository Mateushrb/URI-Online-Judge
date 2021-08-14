# Variáveis necessárias
I = 0
J = 0

# Estruturas de repetição com condição
for i in range(0, 11, 1):
    for l in range(0, 3, 1):
        J += 1
        print("I=%s J=%s" %(I, J))
    J -= 3
    I += 0.2
    J += 0.2
    I = round(I, 1)
    J = round(J, 1)
    if I == 1 or I == 2 or I == 0:
        I = int(I)
        J = int(J)
