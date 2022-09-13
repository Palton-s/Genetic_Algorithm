import crossover
import mutacao
import populacao
import avaliacao as av
import funcoes_auxiliares as aux
import numpy as np
import csv
from dados import *
import matplotlib.pyplot as plt
import time


class GA(Dados):

    def __init__(self, n_geracoes=Dados.n_geracoes, limites_dif=[], mudar_limites=False, N = 0) -> None:
        self.n_geracoes = n_geracoes
        # self.limites = [[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000],[-1000, 1000]]
        # self.limites = [[2.8823580029711597, 2.8823580030196663], [0.001151012790312193, 0.001151012838818577], [-2.796630859423506, -2.7966308593749996], [2.7925618489098274, 2.792561848958334], [3.828126024648858, 3.8281260246973643]]
        # self.limites = [[2.8645833333333406, 2.994791666666674], [0.0, 0.006510416666666667], [-79.03645833333333, -78.90625], [78.90625, 79.03645833333334], [2.03125, 2.037760416666667]]
        #self.limites = [[30, 60], [0, 6], [0, 10]]
        #self.limites = [[0, 1000], [0, 300], [0, 200], [0, 200]]
        if len(limites_dif) > 0:
            self.limites = limites_dif
        if N > 0:
            self.N = N
        # super().__init__()
        # inicia a população
        X = populacao.cria_populacao(self.NV, self.N, self.n_bits)
        # variavel com dados estatísticos de cada geração
        dados_geracao = []
        avaliacoes = []
        for i in range(self.n_geracoes):
            # avalia a população
            limites = self.limites
            Y = av.avaliacao(X, limites)
            # ordena a população
            X, Y = aux.ordena(X, Y)
            # print("----------------------------------")
            # print(i, Y[-1])
            # seleciona os indivíduos elite
            elite = X[-int(self.N*self.percent_elite):]
            # seleciona melhores indivíduos
            melhores = crossover.roleta(X, Y, 0.5)
            # realiza cruzamentos entre esses indivíduos
            filhos = crossover.cruza_populacao(
                melhores, self.n_cortes_no_cruzamento)

            if i != self.n_geracoes-1:
                # realiza mutação nos filhos
                filhos = mutacao.mut_pop(
                    filhos, self.taxa_de_mutacao, self.intensidade_da_mutacao)
                # atribui os filhos à população
                X = aux.atribui(X, filhos, elite)

            if mudar_limites and i % self.mudanca_limites == 0 and i != 0:

                elite_values = aux.converte_populacao(elite, self.limites)
                values = aux.converte_populacao(X, self.limites)
                self.write_on_file("Geração: " + str(i) + " - Melhor: " +
                                   str(Y[-1]) + " - Valores: " + str(values[-1]))
                average_evaluate = np.mean(Y[-int(len(Y)/2)])
                print("Geração: " + str(i) + " - Melhor: " +
                      str(round(Y[-1], 2)) + " - Valores: " + str([round(value, 2) for value in aux.converte_individuo(X[-1], self.limites)]))
                biggest_value = [max([elite_values[i][j] for i in range(
                    len(elite_values))]) for j in range(self.NV)]
                smallest_value = [min([elite_values[i][j] for i in range(
                    len(elite_values))]) for j in range(self.NV)]

                for i in range(self.NV):
                    if smallest_value[i] == biggest_value[i]:
                        smallest_value[i] = smallest_value[i] - \
                            abs(0.1*smallest_value[i])
                        biggest_value[i] = biggest_value[i] + \
                            abs(0.1*biggest_value[i])
                    range_ = biggest_value[i] - smallest_value[i]
                    self.change_limites(
                        i, smallest_value[i]-abs(0.01*range_), biggest_value[i]+abs(0.01*range_))
                X = [aux.desconverve_individuo(
                    values[k], self.limites, self.n_bits) for k in range(self.N)]
            average_evaluate = np.mean(Y[-int(len(Y)/2)])
            print("Geração: " + str(i) + " - Media ava: " + str(average_evaluate) + " - Melhor: " + str(round(Y[-1], 2)) + " - Valores: " + str([round(value, 2) for value in aux.converte_individuo(X[-1], self.limites)]))
            # write on file "grafico_convergencia.csv"

            # now = time.time()
            # now_time = time.strftime("%d %H:%M:%S", time.localtime(now))
            # self.add_to_file("grafico_convergencia.csv", [now_time, i, round(Y[-1], 2), [[round(value_, 2) for value_ in value] for value in self.limites]])
            # populacao_valores = aux.converte_populacao(X, self.limites)
            # del Y, elite, melhores, filhos
            # get the usage cpu percentage
            # self.X = X
            # self.Y = Y

        X, Y = aux.ordena(X, Y)
        self.best_individual = aux.converte_individuo(X[-1], self.limites)
        self.best_evaluation = Y[-1]
        self.values = aux.converte_populacao(X, self.limites)
        print("Melhor indivíduo: ", self.best_evaluation)

    def add_to_file(self, file_name, array):
        # add array data to a csv file
        with open(file_name, 'a') as f:
            csv.writer(f, delimiter=";", lineterminator="\n").writerow(array)

    def plot_result(self):

        values = self.values[-1]
        A = values[0]
        B = values[1]
        C = values[2]

        x = [1+0.3*i for i in range(15)]
        y = [self.potential(45, 0.5, 3, value) for value in x]

        potentials = [self.potential(A, B, C, x_) for x_ in x]

        print(potentials)

        # plot r x potentials and r x HF in sabe plot
        plt.plot(x, potentials, label='potential')
        plt.plot(x, y, label='HF')
        plt.legend()
        plt.show()

    # potential(individuo[0], [individuo[1], individuo[2], individuo[3]], R[i], individuo[4])
    def potential(self,A, B, C, x):
        result = A+1/(B*np.sqrt(2*np.pi))*np.exp(-((x-C)**2)/(2*B**2))
        return result

    def write_on_file(self, text):
        # write text on file "melhores_avaliacoes.log"
        with open("melhores_avaliacoes.log", 'a') as f:
            f.write(text)
            f.write("\n")


"""ga = GA(100, mudar_limites=True)
ga.plot_result()"""
