import random

def cria_populacao(precisao):
    # inicia a populacao
    X = []
    # para cada indivíduos
    for i in range(precisao):
        X.append(i)
    # retorna a populacao
    return X