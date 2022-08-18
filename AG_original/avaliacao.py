from tokenize import Double
import numpy as np
import funcoes_auxiliares as aux
from dados import *

def avaliacao(X, limites):
    Y = []
    individuos = aux.converte_populacao(X, limites)
    for individuo in individuos:
        # define "avaliacao" as much precise as possible
        avaliacao = potential(individuo)
        Y.append(avaliacao)
    return Y

def potential(individuo):
    expoente = 0
    for i in range(len(individuo)):
        expoente += (individuo[i] - 50)**2
    return np.exp(-expoente/100**2)