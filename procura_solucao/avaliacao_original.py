from cmath import sqrt
import numpy as np
import funcoes_auxiliares as aux
from dados import *


def avaliacao(X, limites):

    # inicia a variável que contêm a avaliação
    Y = []
    # converte os cromossomos binários para decimais
    if(limites == [-100, 100]):
        print("Erro")
    X = aux.converte_populacao(X, limites)
    # avalia quão bons os indivíduos são com base em uma gaussiana de variaveis dimensões
    for individuo in X:
        # para cada variável
        avaliacao = ava(individuo)
        
        Y.append(avaliacao)
    return Y

def ava(individuo):
    # exp (x-500)^2 (y-500)^2
    exp_sum = 0
    for i in range(len(individuo)):
        exp_sum += (individuo[i]-500)**2
    avaliacao = np.exp(-exp_sum/(0.03**2))
    return avaliacao


