from cmath import sqrt
import numpy as np
import funcoes_auxiliares as aux
from dados import *


def avaliacao(X, limites):
    table_s2 = [[1.00, -2.861030, -2.904236, -2.90461],
        [1.05, -2.881138, -2.924612, -2.92505],
        [1.10, -2.896661, -2.940398, -2.94060],
        [1.20, -2.917296, -2.961529, -2.96182],
        [1.30, -2.928109, -2.972775, -2.97320],
        [1.40, -2.932502, -2.977519, -2.97798],
        [1.42, -2.932825, -2.977901, -2.97835],
        [1.44, -2.932998, -2.978130, -2.97841],
        [1.4632, -2.933029, -2.978221, -2.97869],
        [1.48, -2.932948, -2.978179, -2.97860],
        [1.50, -2.932747, -2.978022, -2.97844],
        [1.60, -2.930379, -2.975811, -2.97626],
        [1.70, -2.926438, -2.971930, -2.97230],
        [1.80, -2.921631, -2.967091, -2.96761],
        [1.90, -2.916436, -2.961783, -2.96212],
        [2.00, -2.911170, -2.956339, -2.95674],
        [2.20, -2.901175, -2.945856, -2.94606],
        [2.40, -2.892510, -2.936624, -2.93717],
        [2.60, -2.885395, -2.928959, -2.92956],
        [2.80, -2.879755, -2.922839, -2.92341],
        [3.00, -2.875393, -2.918087, -2.91860],
        [3.20, -2.872075, -2.914472, -2.91507],
        [3.40, -2.869580, -2.911757, -2.91220],
        [3.60, -2.867718, -2.909734, -2.91027],
        [3.80, -2.866330, -2.908232, -2.90862],
        [4.00, -2.865296, -2.907115, -2.90767],
        [4.50, -2.863701, -2.905401, -2.90589],
        [5.00, -2.862888, -2.904532, -2.90504],
        [5.50, -2.862444, -2.904061, -2.90431],
        [6.00, -2.862184, -2.903787, -2.90439],
        [7.00, -2.861918, -2.903506, -2.90370],
        [8.00, -2.861795, -2.903376, -2.90396]
        ]

    # a = col 0 of table_s2
    R = [row[0] for row in table_s2]
    HF = [row[1] for row in table_s2]
    CCSDT = [row[2] for row in table_s2]
    DMC = [row[3] for row in table_s2]
    # inicia a variável que contêm a avaliação
    Y = []
    # recupera o número de indivíduos
    individuos = len(X)
    # recupera o número de variáveis
    variaveis = len(X[0])
    # converte os cromossomos binários para decimais
    if(limites == [-100, 100]):
        print("Erro")
    X = aux.converte_populacao(X, limites)
    # avalia quão bons os indivíduos são com base em uma gaussiana de variaveis dimensões
    for individuo in X:
        # inicia o valor do raio da gaussiana
        raio = 0
        # para cada variável
        avaliacao = 0
        quadratic_sum = 0
        for i in range(len(R)):
            potential_ryd = potential(individuo[0], [individuo[1],individuo[2],individuo[3]], R[i], individuo[4])
            quadratic_sum += ((potential_ryd - HF[i])**2)
        #quadratic_mean = (sqrt(quadratic_sum)/len(R))
        quadratic_mean = (sqrt(quadratic_sum)/len(R))
        #avaliacao = 1/(quadratic_mean)
        avaliacao = quadratic_mean
        avaliacao = avaliacao.real
        Y.append(round(avaliacao,5))
    return Y

def potential(D,a,r,r_eq):
    m = len(a)
    somatorio = 1
    for i in range(m):
        somatorio += a[i]*(r-r_eq)
    #V_ryd = -D*somatorio*np.exp(-a[0]**2)
    arg_exponential = -a[0]*(r-r_eq)
    exponential = float(np.exp(arg_exponential))
    V_ryd = -D*somatorio*exponential
    return V_ryd


