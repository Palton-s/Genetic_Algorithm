import random

def cria_populacao(NV, N, n_bits):
    # inicia a populacao
    X = []
    # para cada indivíduos
    for i in range(N):
        variaveis = []
        # para cada variavel
        for j in range(NV):
            variavel = []
            # para cada bit da variavel
            for k in range(n_bits):
                # adiciona um bit aleatório
                variavel.append(random.randint(0, 1))
            # adiciona a variavel ao indivíduo
            variaveis.append(variavel)
        # adiciona a variavel na populacao
        X.append(variaveis)
    # retorna a populacao
    return X