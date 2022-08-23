from cmath import sqrt
import numpy as np
import funcoes_auxiliares as aux
from dados import *


def avaliacao(X, limites):
    table_s2 = [[1.0, 2.493],
                [1.05, 2.16],
                [1.1, 1.857],
                [1.2, 1.2],
                [1.3, 0.75],
                [1.4, 0.271],
                [1.42, 0.181],
                [1.44, 0.0929],
                [1.46, 0.006132],
                [1.48, -0.0789],
                [1.5, -0.1623],
                [1.6, -0.554],
                [1.7, -0.908],
                [1.8, -1.226],
                [1.9, -1.51],
                [2.0, -1.764],
                [2.2, -2.1],
                [2.4, -2.51],
                [2.6, -2.764],
                [2.8, -2.940],
                [3.0, -3.058],
                [3.2, -3.12],
                [3.4, -3.154],
                [3.6, -3.148],
                [3.8, -3.115],
                [4.0, -3.0],
                [4.5, -2.852],
                [5.0, -2.58],
                [5.5, -2.29],
                [6.0, -2.01],
                [7.0, -1.489],
                [8.0, -1.06]]

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
        # inicia o valor do raio da gaussiana
        raio = 0
        # para cada variável
        avaliacao = 0
        quadratic_sum = 0
        for i in range(len(x)):
            potential_ryd = potential(
                individuo[0], individuo[1], individuo[2], individuo[3], x[i])
            quadratic_sum += ((potential_ryd - y[i])**2)
        #quadratic_mean = (sqrt(quadratic_sum)/len(R))
        quadratic_mean = (sqrt(quadratic_sum)/len(x))
        #avaliacao = 1/(quadratic_mean)
        avaliacao = quadratic_mean
        avaliacao = avaliacao.real
        Y.append(avaliacao)
    return Y


def potential(A, B, C, D, x):
    result = D + A*np.exp(-B*((x-C)**2))
    return result
