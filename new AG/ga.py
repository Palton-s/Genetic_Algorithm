from turtle import color
import crossover
import mutacao
import populacao
import avaliacao as av
import funcoes_auxiliares as aux
import numpy as np
import csv
from dados import *
import plotly.express as px



class GA(Dados):

    def exec_ga(self):
        # inicia a população
        X = populacao.cria_populacao(self.NV, self.N, self.n_bits)
        # variavel com dados estatísticos de cada geração
        dados_geracao = []
        avaliacoes = []
        for i in range(self.n_geracoes):
            # avalia a população
            limites = self.get_limites()
            Y = av.avaliacao(X, limites)
            # ordena a população
            X,Y = aux.ordena(X,Y)
            # seleciona os indivíduos elite
            elite = X[-int(self.N*self.percent_elite):]
            # seleciona melhores indivíduos
            melhores = crossover.roleta(X,Y,0.5)
            # realiza cruzamentos entre esses indivíduos
            filhos = crossover.cruza_populacao(melhores, self.n_cortes_no_cruzamento)
            if i != self.n_geracoes-1:
                #realiza mutação nos filhos
                filhos = mutacao.mut_pop(filhos, self.taxa_de_mutacao, self.intensidade_da_mutacao)
                # atribui os filhos à população
                X = aux.atribui(X, filhos, elite)
            #print(i, Y[-1])
            # geração / avaliação média dos indivíduos / melhor avaliação
            #dados_geracao.append([i, np.mean(Y)])
            dados_geracao.append([i,Y[-1]])
            self.add_to_file('dados_geracao.csv', [i, Y[-1]])
        X, Y = aux.ordena(X, Y)
        return aux.converte_individuo(X[-1],limites)

    def add_to_file(self,file_name, array):
        #add array data to a csv file
        with open(file_name, 'a') as f:
            csv.writer(f, delimiter=";", lineterminator="\n").writerow(array)

            


ga_ = GA()
values = ga_.exec_ga()



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
#potential(individuo[0], [individuo[1], individuo[2], individuo[3]], R[i], individuo[4])
def potential(D,a,r,r_eq):
    m = len(a)
    somatorio = 1
    for i in range(m):
        somatorio += a[i]*(r-r_eq)
    V_ryd = -D*somatorio*np.exp(-a[0]**2)
    return V_ryd

D = values[0]
a = [values[1], values[2], values[3]]
r = [row[0] for row in table_s2]
HF = [row[1] for row in table_s2]
r_eq = values[4]

potentials = [potential(D,a,r_,r_eq) for r_ in r]



print(potentials)

#plot r x potentials and r x HF in sabe plot
plt.plot(r,potentials, label='potential')

