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

        with open("./dados_geracao.json", "w") as file:
                file.write("[]")

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





            # Se a mudança de limites estiver ativada e a geração de self.mudanca_limites
            if mudar_limites and i % self.mudanca_limites == 0 and i != 0:
                # Define as larguras mínimas e máximas de cada domínio
                min_ranges = [0.0005,0.0005,0.0005,0.0005]
                max_ranges = [10,10,10,10]
                # Define as dimensões que serão convergidas
                limites_moveis = [True, True, True, True]
                # Seleciona os 20 melhores indivíduos
                selected_values = aux.converte_populacao(X[-20:],self.limites)     
                # Resgata os maiores e menores valores de cada variável
                biggest_value = [max([selected_values[i][j] for i in range(len(selected_values))]) for j in range(self.NV)]
                smallest_value = [min([selected_values[i][j] for i in range(len(selected_values))]) for j in range(self.NV)]
                # Para cada variável
                for k in range(self.NV):
                    # Se a variável for convergível
                    if limites_moveis[k]:
                        # Calcula a diferença entre o maior e o menor valor                        
                        range_ = biggest_value[k] - smallest_value[k]
                        # Se a diferença for menor que o mínimo valor do domínio
                        if range_ < min_ranges[k]:
                            # Ajusta o domínio para o centro dos valores com a largura mínima
                            smallest_value[k] = (smallest_value[k] + biggest_value[k])/2 - min_ranges[k]/2
                            biggest_value[k] = (smallest_value[k] + biggest_value[k])/2 + min_ranges[k]/2
                        # Se a diferença for maior que o máximo valor do domínio
                        if range_ > max_ranges[k]:
                            # Ajusta o domínio para valores com a largura máxima
                            smallest_value[k] = (smallest_value[k] + biggest_value[k])/2 - max_ranges[k]/2
                            biggest_value[k] = (smallest_value[k] + biggest_value[k])/2 + max_ranges[k]/2
                        # Altera o domínio de busca
                        self.change_limites(k, smallest_value[k]-abs(0.05*range_), biggest_value[k]+abs(0.05*range_))
                # Refaz os cromossomos para os novos domínios
                # Traduz os cromossomos para os valores reais
                values = aux.converte_populacao(X, self.limites)    
                X = [aux.desconverve_individuo(values[k], self.limites, self.n_bits) for k in range(self.N)]
            # Segue com o algoritmo




            average_evaluate = np.mean(Y[-int(len(Y)/2)])
            
            #json_data = self.readJSON("./dados_geracao.json")
            #individuos___ = aux.converte_populacao(X[-50:], self.limites)
            #for m in range(len(individuos___)):
            #    individuos___[m] = sorted(individuos___[m])
            #json_data.append([i, self.limites, aux.converte_populacao(X[-50:], self.limites), Y[-50:]])
            #self.saveJSON(json_data, './dados_geracao.json')
            #print("Geração: " + str(i) + " - Media ava: " + str(average_evaluate) + " - Melhor: " + str(round(Y[-1], 6)) + " - Valores: " + str([round(value, 6) for value in aux.converte_individuo(X[-1], self.limites)])+ ' - Limites: '+str(self.limites))
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
        init = 1
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
        """for i in range(15):
            table_s2.append([init,self.potential(45, 0.5, 3, init)])
            init += 0.2"""

        x = [row[0] for row in table_s2]
        y = [row[1] for row in table_s2]
        plt.plot(x, y, label='Dados da curva')
        best = self.best_individual
        new_y = []
        for i in range(len(x)):
            a = [best[i] for i in range(1, len(best)-1)]
            new_y.append(self.potential_2(best[0], a, x[i], best[-1]))
        plt.plot(x, new_y, label='Melhor indivíduo', color="red")

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
    def potential(self, A, B, C, x):
        result = A + (1/(B*np.sqrt(2*np.pi)))*np.exp(-((x-C)**2)/(2*(B**2)))
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

        variaveis = [data[i][2] for i in range(len(data))]
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
            plt.plot(geracoes, limites_inferiores[i], label="limite inferior "+str(i), color="red")
            plt.plot(geracoes, limites_superiores[i], label="limite superior "+str(i), color="green")
            for j in range(n_individuos):
                individuo = [parametros[i][k][j] for k in range(n_geracoes)]
                plt.plot(geracoes, individuo, color="blue", alpha=0.2)
            plt.legend()
            plt.xlabel("Gerações")
            plt.ylabel("Valores")
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


        





#ga = GA(400, mudar_limites=True)

#ga.plot_convergencia()
#ga.plot_result()
testes = [False, True]
dados = []
for i in range(2):
    ga = GA(400, mudar_limites=testes[i])
    dados.append(ga.values)


# plot scarter two graphs side by side
fig, (ax1, ax2) = plt.subplots(1, 2)
#subtitulo
ax1.set_title("Algoritmo genético convencional")
ax2.set_title("Algoritmo genético com mudança de limites")
#plot
ax1_data_x = [dados[0][i][0] for i in range(len(dados[0]))]
ax1_data_y = [dados[0][i][1] for i in range(len(dados[0]))]
ax1.scatter(ax1_data_x, ax1_data_y, color="black", alpha=0.2)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax2_data_x = [dados[1][i][0] for i in range(len(dados[1]))]
ax2_data_y = [dados[1][i][1] for i in range(len(dados[1]))]
ax2.scatter(ax2_data_x, ax2_data_y, color="black", alpha=0.2)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
"""plt.xlim(-1, 1)
    plt.ylim(-1, 1)"""
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()

    

    





def plot_scarter(self):
    valores = self.values
    x = [valores[i][0] for i in range(len(valores))]
    y = [valores[i][1] for i in range(len(valores))]
    # plot scarter from -1 to 1
    plt.scatter(x, y, alpha=0.2, color="black")
    #ajust zoom to -1 to 1
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()

