# Quantidade de testes
qtd_testes = int(input())
# Estrutura de repetição
for i in range(0, qtd_testes, 1):
    # Entrada de dados
    palavra = input()
    
    # Primeira passada
    palavra_1 = str()
    for l in palavra:
        # Se o caracter for alfabético, avança 3 na tabela ASCII e adiciona na variável "palavra_1"
        if l.isalpha():
            ASCII = ord(l)
            ASCII += 3
            ASCII = chr(ASCII)
            palavra_1 += ASCII
        else:
            palavra_1 += l
    
    # Segunda passada, inverte a palavra
    palavra_2 = palavra_1[::-1]
    
    metade = int(len(palavra)/2)
    # Terceira passada, diminui 1 na tabela ASCII, da metade em diante
    palavra_3 = palavra_2[:metade]
    for j in range(metade, len(palavra_2), 1):
        ASCII = ord(palavra_2[j])
        ASCII -= 1
        ASCII = chr(ASCII)
        palavra_3 += ASCII

    # Imprime o resultado
    print(palavra_3)
