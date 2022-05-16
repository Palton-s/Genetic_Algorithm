# importa os modulos necessarios
from telnetlib import GA
import crossover as cross
import mutacao as m
import populacao
import avaliacao as av
import funcoes_auxiliares as aux
import numpy as np

# generate 8 colors
color1 = [200,25,55]
color2 = [31,28,30]
color3 = [43,42,138]
color4 = [38,60,48]
color5 = [217,195,74]
color6 = [255,255,255]
verde = [0,255,0]
azul = [0,0,255]

# cor alvo
color_alvo = [0,233,21]


def GA_cores(cor_1, cor_2, cor_alvo):


    # define informações da população
    N = 1000 # numero de individuos
    percent_elite = 0.1 # percentual dos melhores indivíduos
    n_geracoes = 50 # número de gerações
    taxa_de_mutacao = 0.5 # taxa de mutação
    precisao = 50

    # inicia a população
    X = populacao.cria_populacao(N, precisao)
    for i in range(n_geracoes):
        # avalia a população
        Y = av.avaliacao(X, cor_1, cor_2, cor_alvo, precisao)
        # ordena a população e as avaliações
        X, Y = aux.ordena(X, Y)
        # mostra o melhor indivíduo da geração
        h = aux.calcula_h(X[-1], cor_1, cor_2, cor_alvo)
        print(i, h)
        # seleciona os melhores indivíduos
        elite = X[:int(N*percent_elite)]
        # seleciona os indivíduos para cruzamento
        individuos_para_cruzamento = X[int(N*0.5):]
        # realiza cruzamentos entre esses indivíduos, retornando os filhos
        filhos = cross.cruza_populacao(individuos_para_cruzamento)
        # atribui os filhos à população junto com os indivíduos elite
        X = aux.atribui(X, filhos, elite)
    h = aux.calcula_h(X, cor_1, cor_2, cor_alvo)
    print(h)
        



GA_cores(verde, azul, color_alvo)

        