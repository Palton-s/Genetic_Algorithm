import random

def cria_populacao(N, precisao):
    # inicia a populacao
    X = []
    # para cada indivíduos
    for i in range(N):
        X.append(random.randint(0,precisao))
    # retorna a populacao
    return X