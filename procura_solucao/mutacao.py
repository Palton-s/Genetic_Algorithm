import random

def mutacao_cromossomo_binario(binario, intensidade):
    # percorre cada bit do cromossomo
    for j in range(len(binario)):
        # dada a probabilidade de mutação, altera o bit de 0 para 1 ou de 1 para 0
        if random.uniform(0, 1) < intensidade:
            if binario[j] == 1:
                binario[j] = 0
            else:
                binario[j] = 1
    # retorna o cromossomo binário mutado
    return binario

def mut_pop(X, taxa_de_mutacao, intensidade_da_mutacao):
    # para cada indivíduo
    for i in range(len(X)):
        # para cada variavel
        for j in range(len(X[i])):
            # dada a probabilidade de mutação, altera o bit de 0 para 1 ou de 1 para 0
            if random.uniform(0, 1) < taxa_de_mutacao:
                X[i][j] = mutacao_cromossomo_binario(X[i][j], intensidade_da_mutacao)
    # retorna a populacao mutada
    return X