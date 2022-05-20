# importa os modulos necessarios
from telnetlib import GA
import crossover as cross
import mutacao as m
import populacao
import avaliacao as av
import funcoes_auxiliares as aux
import numpy as np
from manim import *


paleta = [ [200,25,55], [31,28,30], [43,42,138], [38,60,48], [217,195,74], [255,255,255], [0,255,0], [0,0,255] ]

# cor alvo



def cores(cor_1, cor_2, cor_alvo):

    precisao = 10

    # inicia a população
    X = populacao.cria_populacao(precisao)

    # avalia a população
    Y = av.avaliacao(X, cor_1, cor_2, cor_alvo, precisao)
    # ordena a população e as avaliações
    X, Y = aux.ordena(X, Y)
    
    cor_final = aux.mistura_cores(cor_1, cor_2, X[-1], precisao-X[-1])

    # calcula a matiz da cor final
    h_final, s_final, l_final = aux.calcula_hls(cor_final)
    # calcula a matiz da cor alvo
    h_alvo, s_alvo, l_alvo = aux.calcula_hls(cor_alvo)
    # mostra o melhor indivíduo da geração
    h = 1 - av.distancia_circular(h_final, h_alvo)
    proporcao_1 = round(100*X[-1]/precisao,0)
    proporcao_2 = round(100*(precisao-X[-1])/precisao,0)
    return Y[-1],[proporcao_1, proporcao_2], [cor_1, cor_2], cor_alvo,cor_final
        
cor_alvo = [0,150,19]
# tenta todas as combinações de cores possíveis

def procura_melhores_cores(paleta, cor_alvo):
    testes_cores = []
    for i in range(len(paleta)):
        for j in range(len(paleta)):
            cor_1 = paleta[i]
            cor_2 = paleta[j]
            teste_cor = cores(cor_1, cor_2, cor_alvo)
            testes_cores.append(teste_cor)

    # remove odd testes_cores elements
    testes_cores = testes_cores[::2]

    # seleciona os 10 melhores
    testes_cores = sorted(testes_cores, key=lambda x: x[0])[:10]


    return testes_cores[-5:]

def procura_melhor_cinza(cor_alvo, cor_obtida, precisao):
    # testa cada tom de cinza
    misturas = []
    for i in range(256):
        cinza = [i,i,i]
        testes_cinza = []
        #testa todas as proporções possíveis
        for j in range(precisao):
            teste_cor = aux.mistura_cores(cinza, cor_obtida,j, precisao-j)
            proximidade = aux.proximidade_de_cores_RGB(teste_cor, cor_alvo)
            testes_cinza.append([proximidade, teste_cor, cinza, [j, precisao-j]])
        # seleciona o melhor
        testes_cinza = sorted(testes_cinza, key=lambda x: x[0])[-1:]
        misturas.append(testes_cinza[0])
    # seleciona o melhor
    misturas = sorted(misturas, key=lambda x: x[3][0])[-1:]
    return misturas[0]



        
