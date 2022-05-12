import numpy as np
import funcoes_auxiliares as aux


def avaliacao(X):
    # define o dominio de cada variavel
    limites = [-2, 2]
    # inicia a variável que contêm a avaliação
    Y = []
    # recupera o número de indivíduos
    individuos = len(X)
    # recupera o número de variáveis
    variaveis = len(X[0])
    # converte os cromossomos binários para decimais
    X = aux.converte_populacao(X, limites)
    # avalia quão bons os indivíduos são com base em uma gaussiana de variaveis dimensões
    for i in range(individuos):
        # inicia o valor do raio da gaussiana
        raio = 0
        # para cada variável
        for j in range(variaveis):
            # adiciona a avaliação da variável ao indivíduo
            raio += X[i][j]**2
        raio = np.sqrt(raio)
        # calcula a exponencial
        #avaliacao = np.exp(-raio**2)
        s2 = 0.15
        #avaliacao = (np.cos(4*np.pi*raio)**2)*np.exp(-raio**2/s2)
        #avaliacao = (np.cos(3*np.pi*raio)**2)*np.exp(-raio**2)
        x = X[i][0]
        y = X[i][1]
        r1 = (x)**2 + (y)**2
        r2 = (x-0.3)**2 + (y-0.3)**2
        avaliacao = 0.8*np.exp(-(r1 )/(0.3**2))+1*np.exp(-(r2 )/(0.03**2))
        #avaliacao = np.exp(-raio**2)
        Y.append(avaliacao)
    return Y
