import random

def crossover(cromossomo1, cromossomo2, n_cortes):
    # pega o numero de bits do cromossomo
    n_bits = len(cromossomo1)
    # escolhe aleatoriamente os cortes
    crossover_points = random.sample(range(0, n_bits), n_cortes)
    # ordena os cortes
    crossover_points.sort()
    # gera com cromossomo 1 como uma lista de bits todos zerados
    cromossomo_filho_1 = cromossomo1.copy()
    # gera com cromossomo 2 como uma lista de bits todos zerados
    cromossomo_filho_2 = cromossomo2.copy()
    # executa o crossover
    for i in range(len(crossover_points)-1):
        # pega o número de cortes
        if i % 2 == 0:
            # como os filhos são clones dos respectivos pais, basta alterar os grupos pares de bits
            # assim se i for par, 
            # pega o bit do pai 2 e coloca no filho 1
            # e pega o bit do pai 1 e coloca no filho 2
            aux1 = cromossomo1[crossover_points[i]:crossover_points[i+1]].copy()
            aux2 = cromossomo2[crossover_points[i]:crossover_points[i+1]].copy()
            cromossomo_filho_1[crossover_points[i]:crossover_points[i+1]] = aux2
            cromossomo_filho_2[crossover_points[i]:crossover_points[i+1]] = aux1
    # retorna os cromossomos filhos
    # return the first 1/4 bits from the original
    
    cromossomo_filho_1[n_bits-1] = cromossomo1[n_bits-1]
    cromossomo_filho_2[n_bits-1] = cromossomo2[n_bits-1]
    return cromossomo_filho_1, cromossomo_filho_2

def seleciona_pares(melhores):
    # seleciona os pares de indivíduos
    # para a próxima geração
    # seleciona aleatoriamente
    # os indivíduos
    pares = random.sample(melhores, 2)
    # retorna os pares
    return pares

def cruza_populacao(melhores, n_cortes):
    # resgata o número de cruzamentos
    n_cruzamentos = len(melhores)
    # inicia a população de filhos
    filhos = []
    # para cada cruzamento
    for i in range(n_cruzamentos):
        # seleciona os pares de indivíduos
        pares = seleciona_pares(melhores)
        n_variaveis = len(pares[0])
        variaveis = []
        # para cada variavel
        filho_1 = []
        filho_2 = []
        for j in range(n_variaveis):
            variavel_filho1 = []
            variavel_filho2 = []
            # realiza o crossover das suas variáveis
            variavel_filho1, variavel_filho2 = crossover(pares[0][j], pares[1][j], n_cortes)
            # adiciona a variavel ao novo indivíduo
            filho_1.append(variavel_filho1)
            filho_2.append(variavel_filho2)
        # adiciona os filhos na população de filhos
        filhos.append(filho_1)
        filhos.append(filho_2)
    # retorna a população de filhos
    return filhos

def cruza_individuos(individuo1, individuo2, n_cortes):
    n_variaveis = len(individuo1)
    filho_1 = []
    filho_2 = []
    for j in range(n_variaveis):
        variavel_filho1 = []
        variavel_filho2 = []
        # realiza o crossover das suas variáveis
        variavel_filho1, variavel_filho2 = crossover(individuo1[j], individuo2[j], n_cortes)
        # adiciona a variavel ao novo indivíduo
        filho_1.append(variavel_filho1)
        filho_2.append(variavel_filho2)
    # retorna os filhos
    return [filho_1, filho_2]


def roleta(X,Y,percent_individuos):
    # pega a quantidade de indivíduos
    n_individuos = len(X)
    # pega a quantidade de indivíduos que serão selecionados
    n_individuos_selecionados = int(percent_individuos * n_individuos)
    # inicia a população de filhos
    filhos = []
    roleta_vals = []
    # para cada indivíduo da população adiciona uma fração da roleta proportional ao seu fitness
    for i in range(n_individuos):
        roleta_vals.append(Y[i]/sum(Y))
    # soma todas as frações
    soma_roleta = sum(roleta_vals)
    # para cada indivíduo da população
    for i in range(n_individuos):
        # pega a fração da roleta
        roleta_vals[i] = 360*roleta_vals[i]/soma_roleta
    # para cada indivíduo a ser selecionado
    for i in range(n_individuos_selecionados):
        # pega o valor da roleta
        valor_roleta = random.randint(0,360)
        # inicia uma soma
        soma = 0
        # pega o indivíduo que está na posição da roleta
        for j in range(n_individuos):
            soma += roleta_vals[j]
            selecionou = False
            if soma >= valor_roleta:
                # adiciona o indivíduo na população de filhos
                selecionou = True
                filhos.append(X[j])
                break
        if not selecionou:
            filhos.append(X[n_individuos-1])
    # retorna a população de filhos
    return filhos

import funcoes_auxiliares as aux
import numpy as np


def get_best_desvio(n_cortes__):
    cortes = [i+1 for i in range(n_cortes__ -1)]
    desvios_padrao = []
    medias = []
    sup = []
    inf = []
    dados_gerais = []
    for i in range(n_cortes__ -1):
        cromossomo_1 = []
        cromossomo_2 = []
        
        for j in range(n_cortes__):
            cromossomo_1.append(0)
            cromossomo_2.append(1)
        individuo_1 = [cromossomo_1]
        individuo_2 = [cromossomo_2]
        n_cortes = cortes[i]


        dados = []
        for j in range(10000):
            ranges = [[-100,100]]
            lim_inf = -random.randint(0,100)
            lim_sup = random.randint(0,100)
            filho_1, filho_2 = cruza_individuos(individuo_1, individuo_2, n_cortes)
            val = aux.converte_individuo(filho_1, ranges)
            val_2 = aux.converte_individuo(filho_2, ranges)
            dados.append(max([val[0], val_2[0]]))
            


        desvios_padrao.append((np.std(dados))/((100-(-100))/2))
        medias.append(np.mean(dados))
        sup.append(np.mean(dados)+np.std(dados))
        inf.append(np.mean(dados)-np.std(dados))
        #dados_gerais.append(dados)


        val_filho_1 = aux.converte_individuo(filho_1, ranges)
        val_filho_2 = aux.converte_individuo(filho_2, ranges)
    max_std = max(desvios_padrao)
    max_std_index = desvios_padrao.index(max_std)
    return [n_cortes__,cortes[max_std_index]]

import matplotlib.pyplot as plt

"""values = []
for i in range(5, 30):
    values.append(get_best_desvio(i))
    print(i, values[-1])
print(values)
x = [i[0] for i in values]
y = [i[1] for i in values]"""
x = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
y = [2,2,2,2,2,2,3,3,3,3,3,4,4,4,5,5,5,6,6,6,6,6,7,7,7]

plt.plot(x, y)
plt.xlabel('Número de bits')
plt.ylabel('Melhor número de cortes')
#plt.plot(cortes, medias)
#plt.plot(cortes, sup)
#plt.plot(cortes, inf)
"""for i in range(len(dados_gerais)):
    #scartter plot
    for j in range(len(dados_gerais[i])):
        plt.scatter(cortes[i], dados_gerais[i][j], color='black', alpha=0.5)"""
#plt.xlabel('Número de cortes')
#plt.ylabel('Desvio padrão dos indivíduos')
plt.show()