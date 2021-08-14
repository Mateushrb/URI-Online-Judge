novo_calculo = 1 # Variável de condição para repetição
while novo_calculo == 1: # Estrutura de repetição
    
    # Variável para condição da estrutura de repetição para nota válida 1
    nota_valida_1 = 0
    
    while nota_valida_1 != 1: # Estrutura de repetição de nota válida 1
        nota_1 = float(input()) # Entrada da nota 1
        
        # Condição para nota válida 1
        if nota_1 >= 0 and nota_1 <= 10:
            nota_valida_1 = 1
        else:
            print("nota invalida") # Impressão se a nota for inválida
    
    # Variável para condição da estrutura de repetição para nota válida 2
    nota_valida_2 = 0
    
    while nota_valida_2 != 1: # Estrutura de repetição de nota válida 2
        nota_2 = float(input()) # Entrada da nota 2
        
        # Condição para nota válida 2
        if nota_2 >= 0 and nota_2 <= 10:
            nota_valida_2 = 1
        else:
            print("nota invalida") # Impressão se a nota for inválida
    
    media = (nota_1 + nota_2) / 2 # Cálculo da média
    print("media = %0.2f" %(media)) # Impressão da média
    
    # Condição para estrutura de repetição de um novo cálculo
    rep = 0
    while rep == 0: # Estrutura de repetição de novo cálculo
        print("novo calculo (1-sim 2-nao)") # Impressão da pergunta
        novo_calculo = float(input()) # Resposta da pergunta
        
        #Estrutura de condição de novo cálculo
        if novo_calculo < 1 or novo_calculo > 2:
            rep = 0
        else:
            rep = 1

