from cmath import sqrt
import numpy as np
import funcoes_auxiliares as aux
from dados import *


def avaliacao(X, limites):
    table_s2 = [[1.1, 63.40135055],
                [1.2, 64.90544146],
                [1.3, 66.60857345],
                [1.4, 68.51167852],
                [1.5, 70.60936103],
                [1.6, 72.88899945],
                [1.7, 75.33008112],
                [1.8, 77.90385152],
                [1.9, 80.5733492],
                [2, 83.29387969],
                [2.1, 86.01395649],
                [2.2, 88.67670667],
                [2.3, 91.22170422],
                [2.4, 93.58715951],
                [2.5, 95.71236062],
                [2.6, 97.54023559],
                [2.7, 99.01988668],
                [2.8, 100.1089403],
                [2.9, 100.7755616],
                [3, 101],
                [3.1, 100.7755616],
                [3.2, 100.1089403],
                [3.3, 99.01988668],
                [3.4, 97.54023559],
                [3.5, 95.71236062],
                [3.6, 93.58715951],
                [3.7, 91.22170422]]

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
