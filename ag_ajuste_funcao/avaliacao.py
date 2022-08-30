from cmath import sqrt
import numpy as np
import funcoes_auxiliares as aux
from dados import *


def avaliacao(X, limites):
    init = 1
    table_s2 = []
    for i in range(30):
        table_s2.append([init,potential(45, 0.5, -20, init)])
        init += 0.1

    # a = col 0 of table_s2
    x = [row[0] for row in table_s2]
    y = [row[1] for row in table_s2]

    Y = []
    # recupera o número de indivíduos
    individuos = len(X)
    # recupera o número de variáveis
    variaveis = len(X[0])
    # converte os cromossomos binários para decimais
    X = aux.converte_populacao(X, limites)
    # avalia quão bons os indivíduos são com base em uma gaussiana de variaveis dimensões
    for individuo in X:
        # para cada variável
        avaliacao = 0
        quadratic_sum = 0
        for i in range(len(x)):
            potential_ryd = potential(individuo[0], individuo[1], individuo[2], x[i])
            quadratic_sum += ((potential_ryd - y[i])**2)
        #quadratic_mean = (sqrt(quadratic_sum)/len(R))
        quadratic_mean = (sqrt(quadratic_sum)/len(x))
        #avaliacao = 1/(quadratic_mean)
        avaliacao = quadratic_mean
        avaliacao = avaliacao.real
        Y.append(avaliacao)
    return Y


def potential(A, B, C, x):
    result = A + (1/(B*np.sqrt(2*np.pi)))*np.exp(-((x-C)**2)/(2*(B**2)))

    return result

