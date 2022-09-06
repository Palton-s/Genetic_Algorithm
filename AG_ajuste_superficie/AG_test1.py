from turtle import color
import crossover
import mutacao
import populacao
import avaliacao as av
import funcoes_auxiliares as aux
import numpy as np
import csv
from dados import *

class GA():
    def __init__(self, n_individuos, n_geracoes, taxa_mutacao, taxa_crossover, limites, funcao_avaliacao, funcao_criacao, funcao_mutacao, funcao_crossover):
    # inicia a população
    X = populacao.cria_populacao(NV, N, n_bits)
    # variavel com dados estatísticos de cada geração
    dados_geracao = []
    avaliacoes = []
    for i in range(n_geracoes):
        # avalia a população
        Y = av.avaliacao(X)
        # ordena a população
        X,Y = aux.ordena(X,Y)
        # seleciona os indivíduos elite
        elite = X[-int(N*percent_elite):]
        # seleciona melhores indivíduos
        melhores = crossover.roleta(X,Y,0.5)
        # realiza cruzamentos entre esses indivíduos
        filhos = crossover.cruza_populacao(melhores, n_cortes_no_cruzamento)
        if i != n_geracoes-1:
            #realiza mutação nos filhos
            filhos = mutacao.mut_pop(filhos, taxa_de_mutacao, intensidade_da_mutacao)
        # atribui os filhos à população
        X = aux.atribui(X, filhos, elite)
        #print(i, Y[-1])
        # geração / avaliação média dos indivíduos / melhor avaliação
        #dados_geracao.append([i, np.mean(Y)])
        dados_geracao.append([i,Y[-1]])
        add_to_file('dados_geracao.csv', [i,np.mean(Y[-150:])])
    X, Y = aux.ordena(X, Y)
    return aux.converte_individuo(X[-1],[-100, 100])

def add_to_file(file_name, array):
    #add array data to a csv file
    with open(file_name, 'a') as f:
        csv.writer(f, delimiter=";", lineterminator="\n").writerow(array)

        

dados = GA(NV, N, n_bits, percent_elite, n_cortes_no_cruzamento, n_geracoes, taxa_de_mutacao, intensidade_da_mutacao)
add_to_file('dados_geracao.csv', dados)
print("dados")