# Primeira entrada de dados
# Notas
N1, N2, N3, N4 = [float(x) for x in input().split()]

# Pesos das notas
Peso_N1 = 2
Peso_N2 = 3
Peso_N3 = 4
Peso_N4 = 1

# Cálculo da média
media = (N1*Peso_N1 + N2*Peso_N2 + N3*Peso_N3 + N4*Peso_N4) / (Peso_N1 + Peso_N2 + Peso_N3 + Peso_N4)

# Primeira saída de dados
print("Media: %0.1f" %media)

# Seleção das condições
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    # Segunda entrada de dados
    nota_exame = float(input())
    print("Nota do exame: %0.1f" %nota_exame)
    nota_final = (media + nota_exame) / 2
    if nota_final >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %0.1f" %nota_final)
