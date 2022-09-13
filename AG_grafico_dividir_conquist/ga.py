import crossover
import mutacao
import populacao
import avaliacao as av
import funcoes_auxiliares as aux
import numpy as np
import csv
import matplotlib.pyplot as plt
import time


class Dados():    
    # define informações da população
    mudanca_limites = 2
    NV = 2  # número de variáveis
    N = 1000 # numero de individuos
    n_bits = 10 # número de bits por variável em cada indivíduo
    percent_elite = 0.01 # percentual dos melhores indivíduos que serão conservados para a próxima geração
    n_cortes_no_cruzamento = int(n_bits/3) # número de pontos de corte no cruzamento
    n_geracoes = 3000 # número de gerações
    taxa_de_mutacao = 0.6 # taxa de mutação
    intensidade_da_mutacao = 0.2 # intensidade da mutação
    limites = []
    for i in range(NV):
        limites.append([-3, 3])

    def change_limites(self, variable, range1, range2):
        self.limites[variable] = [range1, range2]
        return self.limites
    
    def get_limites(self):
        return self.limites
    def set_limites(self, limites):
        self.limites = limites
        return self.limites

class GA(Dados):

    def __init__(self, n_geracoes = Dados.n_geracoes, limites_dif = [], mudar_limites = False ) -> None:
        self.n_geracoes = n_geracoes
        #self.limites = [[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000]]
        if len(limites_dif) > 0:
            self.limites = limites_dif
        #super().__init__()
        # inicia a população
        X = populacao.cria_populacao(self.NV, self.N, self.n_bits)
        # variavel com dados estatísticos de cada geração
        dados_geracao = []
        avaliacoes = []
        melhores_valores__ = []
        for i in range(self.n_geracoes):
            # avalia a população
            limites = self.limites
            Y = av.avaliacao(X, limites)
            # ordena a população
            X,Y = aux.ordena(X,Y)
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

            if mudar_limites and i % self.mudanca_limites == 0 and i != 0:
                
                elite_values = aux.converte_populacao(elite, self.limites)
                values = aux.converte_populacao(X, self.limites)
                self.write_on_file("Geração: " + str(i) + " - Melhor: " + str(Y[-1]) + " - Valores: " + str(values[-1]))
                average_evaluate = np.mean(Y)
                print("Geração: " + str(i) + " - Melhor: " + str(Y[-1]) + " - Valores: " + str(values[-1]))
                biggest_value = [max([elite_values[i][j] for i in range(len(elite_values))]) for j in range(self.NV)]
                smallest_value = [min([elite_values[i][j] for i in range(len(elite_values))]) for j in range(self.NV)]

                for i in range(self.NV):
                    if smallest_value[i] == biggest_value[i]:
                        smallest_value[i] = smallest_value[i] - abs(0.1*smallest_value[i])
                        biggest_value[i] = biggest_value[i] + abs(0.1*biggest_value[i])
                        
                    self.change_limites(i, smallest_value[i]-abs(0.3*smallest_value[i]), biggest_value[i]+abs(0.3*biggest_value[i]))
                X = [aux.desconverve_individuo(values[k], self.limites, self.n_bits) for k in range(self.N)]
            melhor_individuo = Y[-1]
            melhores_avaliacoes = Y[-20:]
            melhores_valores = aux.converte_populacao(X[-20:], self.limites)
            avaliacoes.append(melhores_avaliacoes)
            melhores_valores__.append(melhores_valores)
            
            print("Geração: " + str(i) + " - Melhor: " + str(melhor_individuo))
            # plot scarter
            """plt.scatter([individuos[i][0] for i in range(len(individuos))], [individuos[i][1] for i in range(len(individuos))], s=1)
            plt.show()"""
            
            
        X, Y = aux.ordena(X, Y)
        self.best_individual = aux.converte_individuo(X[-1], self.limites)
        self.best_evaluation = Y[-1]
        self.values = aux.converte_populacao(X, self.limites)
        self.avaliacoes = avaliacoes
        self.melhores_valores = melhores_valores__
        #plot line avaliacoes
        """for i in range(len(avaliacoes[0])):
            plt.plot([avaliacoes[j][i] for j in range(len(avaliacoes))])
        plt.show()"""
        print("Melhor indivíduo: ", self.best_evaluation)

ga = GA(20, mudar_limites = False)
