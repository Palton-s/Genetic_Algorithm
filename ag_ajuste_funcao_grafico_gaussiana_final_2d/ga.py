from turtle import color
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
import json


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
        dados_grafico_limites = []
        for i in range(self.n_geracoes):
            #time.sleep(1)
            # avalia a população
            limites = self.limites
            Y = av.avaliacao(X, limites)
            # ordena a população
            X, Y = aux.ordena(X, Y)
            ###########################################
            ###########################################
            ###########################################
            limites_grafico = []
            for k in range(self.NV):
                limites_grafico.append([self.limites[k][0], self.limites[k][1]])
                n_coleta = 20
                for j in range(n_coleta):
                    limites_grafico[k].append(aux.converte_individuo(X[-(j+1)], self.limites)[k])
            dados_grafico_limites.append([i,limites_grafico])
            # write on file dados_grafico_evolucao
            self.add_to_file("dados_grafico_evolucao.csv", limites_grafico)
            ###########################################
            ###########################################
            ###########################################
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
            """if Y[-1] < 0.01:
                self.taxa_de_mutacao = 0.5 # taxa de mutação
                self.intensidade_da_mutacao = 0.5 # intensidade da mutação"""
            if mudar_limites and i % self.mudanca_limites == 0 and i != 0:
                min_ranges = [50/i,50/i,50/i,50/i]
                max_ranges = [50/i,50/i,50/i,50/i]
                """for n in range(self.NV):
                    min_ranges.append(1+50/i)
                    max_ranges.append(1+50/i)"""
                """for m in range(self.NV):
                    min_ranges.append(100)
                    max_ranges.append(500)"""
                
                limites_moveis = []
                for m in range(self.NV):
                    limites_moveis.append(True)

                X, Y = aux.ordena(X, Y)
                #selected_values = aux.converte_populacao(elite, self.limites)
                selected_values = aux.converte_populacao(X[-20:],self.limites)
                values = aux.converte_populacao(X, self.limites)
                #self.write_on_file("Geração: " + str(i) + " - Melhor: " + str(Y[-1]) + " - Valores: " + str(values[-1]) + " - Limites: " + str(self.limites))
                average_evaluate = np.mean(Y[-int(len(Y)/2)])
                #print("Geração: " + str(i) + " - Melhor: " + str(round(Y[-1], 2)) + " - Valores: " + str([round(value, 2) for value in aux.converte_individuo(X[-1], self.limites)]))
                biggest_value = [max([selected_values[i][j] for i in range(
                    len(selected_values))]) for j in range(self.NV)]
                smallest_value = [min([selected_values[i][j] for i in range(
                    len(selected_values))]) for j in range(self.NV)]

                for k in range(self.NV):
                    if limites_moveis[k]:
                        if smallest_value[k] == biggest_value[k]:
                            smallest_value[k] = smallest_value[k] - \
                                abs(0.1*smallest_value[k])
                            biggest_value[k] = biggest_value[k] + \
                                abs(0.1*biggest_value[k])
                        range_ = biggest_value[k] - smallest_value[k]
                        if biggest_value[k] - smallest_value[k] < min_ranges[k]:
                            smallest_value[k] = (smallest_value[k] + biggest_value[k])/2 - min_ranges[k]/2
                            biggest_value[k] = (smallest_value[k] + biggest_value[k])/2 + min_ranges[k]/2
                        if biggest_value[k] - smallest_value[k] > max_ranges[k]:
                            smallest_value[k] = (smallest_value[k] + biggest_value[k])/2 - max_ranges[k]/2
                            biggest_value[k] = (smallest_value[k] + biggest_value[k])/2 + max_ranges[k]/2
                        
                        self.change_limites(
                            k, smallest_value[k]-abs(0.05*range_), biggest_value[k]+abs(0.05*range_))
                X = [aux.desconverve_individuo(
                    values[k], self.limites, self.n_bits) for k in range(self.N)]
                teste__ = aux.converte_populacao(X, self.limites)
                print("jaja")
            
            average_evaluate = np.mean(Y[-int(len(Y)/2)])
            # read json './dados_grafico_evolucao.json'
            #json_data = self.readJSON("./dados_geracao.json")
            #json_data.append([i, self.limites, aux.converte_populacao(X[-50:], self.limites), sorted(Y[-50:])])
            #self.saveJSON(json_data, './dados_geracao.json')
            print("Geração: " + str(i) + " - Media ava: " + str(average_evaluate) + " - Melhor: " + str(round(Y[-1], 6)) + " - Valores: " + str([round(value, 6) for value in aux.converte_individuo(X[-1], self.limites)])+ ' - Limites: '+str(self.limites))
            # write on file "grafico_convergencia.csv"

            # now = time.time()
            # now_time = time.strftime("%d %H:%M:%S", time.localtime(now))
            # self.add_to_file("grafico_convergencia.csv", [now_time, i, round(Y[-1], 2), [[round(value_, 2) for value_ in value] for value in self.limites]])
            # populacao_valores = aux.converte_populacao(X, self.limites)
            # del Y, elite, melhores, filhos
            # get the usage cpu percentage
            # self.X = X
            # self.Y = Y
            
        plot_var_data = []    
        """plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True
        for i in range(self.NV):
            values_graph_lines = [x[1][i] for x in dados_grafico_limites]
            index = [x[0] for x in dados_grafico_limites]
            
            min_plot = [x[0] for x in values_graph_lines]
            max_plot = [x[1] for x in values_graph_lines]
            
            # plot line meanplot and minplot and maxplot
            plt.subplot(self.NV, 1, i+1)
            #if i == 0:
            for k in range(20):
                mean_plot = [x[2+k] for x in values_graph_lines]
                plt.plot(index, mean_plot, color="blue", alpha=0.2)
            plt.plot(index, min_plot, label="Domínio mínimo", color="green")
            plt.plot(index, max_plot, label="Domínio máximo", color="red")
            plt.legend()
            plt.xlabel("Nº da geração")
            plt.ylabel("Valor do parâmetro")
            plt.title("Evolução do " + str(i+1)+ "º parâmetro")
        plt.show()
        print("jaja")"""
        # plot line
            


        X, Y = aux.ordena(X, Y)
        self.best_individual = aux.converte_individuo(X[-1], self.limites)
        self.best_evaluation = Y[-1]
        self.values = aux.converte_populacao(X, self.limites)
        #print("Melhor indivíduo: ", self.best_evaluation)
        self.atualiza_count_thread("count.csv")

    def add_to_file(self, file_name, array, delimiter=";"):
        # add array data to a csv file
        with open(file_name, 'a') as f:
            csv.writer(f, delimiter=delimiter, lineterminator="\n").writerow(array)

    def saveJSON(self, array, file_name):
        with open(file_name, 'w') as f:
            json.dump(array, f)
    
    def readJSON(self, file_name):
        with open(file_name, 'r') as f:
            return json.load(f)
    
    def plot_result(self):

        x = [i/20 for i in range(0, 50)]
        y = [self.potential(6.6282, 1.3941, 1.1352, 3.5231, x[i]) for i in range(len(x))]
        
        best = self.best_individual
        bests = self.values[-100:]
        plt.title("Ajuste dos melhores indivíduos")
        for j in range(len(bests)):
            new_y = []
            for i in range(len(x)):
                new_y.append(self.potential(bests[j][0], bests[j][1], bests[j][2], bests[j][3], x[i]))
            plt.plot(x, new_y, label='Melhor indivíduo', color='red', linewidth=0.5, alpha=0.2)
        plt.plot(x, y, label='Dados da curva')
        """for i in range(25):
            A = self.values[-i][0]
            B = self.values[-i][1]
            C = self.values[-i][2]
            potentials = []
            x = []
            init = 1
            for j in range(300):
                potentials.append([init,self.potential(A, B, C, init)])
                x.append(init)
                init += 0.01
            plt.plot(x, potentials, linewidth=0.5, alpha=0.2, color='red')
        plt.legend()"""
        plt.show()

    # potential(individuo[0], [individuo[1], individuo[2], individuo[3]], R[i], individuo[4])
    def potential(self,A, B, C, D, x):
        result = A + B*(x-C)*np.exp(-D*(x-B)**2)
        return result

    def potential_2(self, D, a, r, r_eq):
        m = len(a)
        somatorio = 1
        rho = r - r_eq
        for i in range(1,m+1):
            somatorio += a[i-1]*(rho**i)
        #V_ryd = -D*somatorio*np.exp(-a[0]**2)
        V_ryd = -D*somatorio*np.exp(-a[0]*rho)
        return V_ryd

    def write_on_file(self, text):
        # write text on file "melhores_avaliacoes.log"
        with open("melhores_avaliacoes.log", 'a') as f:
            f.write(text)
            f.write("\n")
    
    def atualiza_count_thread(self, file_name):
        time.sleep(1)
        divider = " ---- "
        # read the last line
        with open(file_name, "r") as f:
            # if file is empty, write 1
            readed = f.read()
            if readed == "":
                with open(file_name, "w") as f:
                    f.write("1"+divider+str(self.best_evaluation)+divider+str(self.limites))
                return
        with open(file_name, "r") as f:
            last_value = f.readlines()[-1]
            last_value = last_value.split(divider)[0]
            # add 1 to the last value
            last_value = int(last_value)+1
            # write the new value on file
        with open(file_name, "a") as f:
            f.write(str(last_value)+divider+str(self.best_evaluation)+divider+str(self.limites)+"\n")

    def plot_convergencia(self):
        #reaf file dados_geracao.json
        with open("dados_geracao.json", "r") as f:
            data = json.load(f)
        #plot
        geracoes = [data[i][0] for i in range(len(data))]

        
        parametros = []
        n_param = len(data[0][1])
        n_geracoes = len(data)
        n_individuos = len(data[0][2])
        parametros = []
        for i in range(n_param):
            parametro = []
            for j in range(n_geracoes):
                parametro.append([data[j][2][k][i] for k in range(n_individuos)])
            parametros.append(parametro)
        limites_inferiores = []
        limites_superiores = []
        for i in range(n_param):
            limites_inf = []
            limites_sup = []
            for j in range(n_geracoes):
                limites_inf.append(data[j][1][i][0])
                limites_sup.append(data[j][1][i][1])
            limites_inferiores.append(limites_inf)
            limites_superiores.append(limites_sup)

        for i in range(n_param):
            plt.plot(geracoes, limites_inferiores[i], label="limite inferior", color="red")
            plt.plot(geracoes, limites_superiores[i], label="limite superior", color="green")
            for j in range(n_individuos):
                individuo = [parametros[i][k][j] for k in range(n_geracoes)]
                plt.plot(geracoes, individuo, color="blue", alpha=0.2)
            # add title
            plt.title("Evolução do parâmetro "+str(i+1))
            # x label
            plt.xlabel("Geração")
            # y label
            plt.ylabel("Valor do parâmetro")
            plt.show()
        avaliacoes = [data[i][3] for i in range(len(data))]
        individuo_avaliacoes = []
        for i in range(n_individuos):
            individuo_avaliacoes.append([avaliacoes[j][i] for j in range(n_geracoes)])
        # plot all
        for i in range(n_individuos):
            plt.plot(geracoes, individuo_avaliacoes[i], alpha=0.4)
        plt.title("Evolução das avaliações")
        plt.xlabel("Geração")
        plt.ylabel("Avaliação")
        plt.show()
ga = GA(1, mudar_limites=False)

ga.plot_convergencia()
ga.plot_result()
