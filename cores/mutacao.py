import random

def mutacao_cromossomo_binario(individuo, intensidade):
    intensidade = intensidade/100

def mut_pop(X, taxa_de_mutacao, intensidade_da_mutacao):
    # para cada indivíduo
    for i in range(len(X)):
        # dada a probabilidade de mutação, altera o bit de 0 para 1 ou de 1 para 0
        if random.uniform(0, 1) < taxa_de_mutacao:
            X[i] = mutacao_cromossomo_binario(X[i], intensidade_da_mutacao)
        
    # retorna a populacao mutada
    return X