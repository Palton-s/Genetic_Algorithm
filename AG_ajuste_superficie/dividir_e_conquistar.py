import re
import threading
from ga import GA
import datetime

#ranges = [[2.5, 3.125], [0.0, 0.3125], [-0.625, 0.0], [0.0, 0.625], [0.125, 0.25]]
#ranges = [[-10,10],[-10,10],[-10,10],[-10,10],[-10,10]]
#ranges = [[-100,100],[0,10],[-100,100],[-100,100],[0,10]]
#ranges = [[5/6,2.5],[5/6,2.5]]
ranges = [[0,180],[0.000001,1.8],[0,15]]

def add_and_reorder(data, divisor,file_name, reverse):

    print(data)
    # save on file file_name
    with open(file_name, "a") as f:
        for i in range(len(data)):
            value =[ str(data[i][j]) for j in range(len(data[i]))]
            row = (divisor.join(value))+"\n"
            f.write(row)

    # read file_name file
    with open(file_name, "r") as f:
        # read tata as array
        testes = f.readlines()
        # remove \n from each element of array
        testes = [testes[i].replace("\n", "") for i in range(len(testes))]
        # split each element of array by " -------- "
        testes = [testes[i].split(divisor) for i in range(len(testes))]
    print("testes")
    # order testes by id
    testes = sorted(testes, key=lambda x: x[0], reverse=reverse)

    # save on file file_name
    with open(file_name, "w") as f:
        for i in range(len(testes)):
            f.write(str(testes[i][0])+divisor+str(testes[i][1])+"\n")

"""def limites_espalhamento(limites, spaces):
    ranges = []
    # ranges = [[[-1000,0,],[-1000,0,],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]]]
    for i in range(spaces):
        for j in range(spaces):
            # i for element 0
            for k in range(spaces):
                for l in range(spaces):
                    for m in range(spaces):
                        limites_var = []
                        limites_var.append([limites[0][0]+i*(limites[0][1]-limites[0][0])/spaces,limites[0][0]+(i+1)*(limites[0][1]-limites[0][0])/spaces])
                        limites_var.append([limites[1][0]+j*(limites[1][1]-limites[1][0])/spaces,limites[1][0]+(j+1)*(limites[1][1]-limites[1][0])/spaces])
                        limites_var.append([limites[2][0]+k*(limites[2][1]-limites[2][0])/spaces,limites[2][0]+(k+1)*(limites[2][1]-limites[2][0])/spaces])
                        limites_var.append([limites[3][0]+l*(limites[3][1]-limites[3][0])/spaces,limites[3][0]+(l+1)*(limites[3][1]-limites[3][0])/spaces])
                        limites_var.append([limites[4][0]+m*(limites[4][1]-limites[4][0])/spaces,limites[4][0]+(m+1)*(limites[4][1]-limites[4][0])/spaces])
                        ranges.append(limites_var)
    return ranges"""
def limites_espalhamento(limites, spaces):
    ranges = []
    # ranges = [[[-1000,0,],[-1000,0,],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]]]
    for i in range(spaces):
        for j in range(spaces):
            for m in range(spaces):
                limites_var = []
                limites_var.append([limites[0][0]+i*(limites[0][1]-limites[0][0])/spaces,limites[0][0]+(i+1)*(limites[0][1]-limites[0][0])/spaces])
                limites_var.append([limites[1][0]+j*(limites[1][1]-limites[1][0])/spaces,limites[1][0]+(j+1)*(limites[1][1]-limites[1][0])/spaces])
                limites_var.append([limites[2][0]+m*(limites[2][1]-limites[2][0])/spaces,limites[2][0]+(m+1)*(limites[2][1]-limites[2][0])/spaces])
                ranges.append(limites_var)
    return ranges


def executa_ga(geracoes, limite,avaliacoes, melhores_valores, melhor_individuo):
    ga = GA(geracoes, limite)
    avaliacoes.append(ga.avaliacoes)
    melhores_valores.append(ga.melhores_valores)
    melhor_individuo.append(ga.melhores_valores)
    
    
        



inicio_da_execucao = datetime.datetime.now()
def exec_thread(limites, n_geracoes):
    threads = []
    avaliacoes = []
    melhores_valores = []
    melhor_individuo = []
    n__ = int(len(limites))
    date_hour_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for i in range(n__):
        print("Thread "+str(i)+" started at "+date_hour_str)
        results = [0] * n__
        threads.append(threading.Thread(target=executa_ga, args=(n_geracoes, limites[i],avaliacoes, melhores_valores, melhor_individuo)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    #add_and_reorder(avaliacoes, " -------- ", "testesss.log", True)

    # order avaliacoes by best_evaluation
    avaliacoes.sort(key=lambda x: x[0])
    print(avaliacoes[0][0])

    # select the first half
    #avaliacoes = avaliacoes[:4]

    print(avaliacoes)
    tempo_fim_execucao = datetime.datetime.now()
    tempo_execucao = (tempo_fim_execucao - inicio_da_execucao).total_seconds()
    print("Tempo de execução: "+str(tempo_execucao)+" segundos")
    with open("esp_dom.log", "a") as f:
        f.write("Tempo de execução: "+str(tempo_execucao)+" segundos\n")
        f.write("----------------------\n")
    return [avaliacoes, melhores_valores, melhor_individuo]

import matplotlib.pyplot as plt
import random
import numpy as np

def potential(A, B, C, x):
    result = A+1/(B*np.sqrt(2*np.pi))*np.exp(-((x-C)**2)/(2*B**2))
    return result.real

limites = limites_espalhamento(ranges,4)
#limites = [[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]]]
half_len = int(len(limites)/2)


while True:
    avaliacoes_finais = []
    avaliacoes = []
    n_geracoes = 50
    #avaliacoes += exec_thread(limites,n_geracoes)
    thr = exec_thread(limites,n_geracoes)
    avaliacoes += thr[0]
    melhores_individuos = thr[1]
    melhores_individuos = thr[2]
    todos_inds = []
    todos_inds_values = []
    for i in range(len(avaliacoes)):
        subdom = avaliacoes[i]
        values_subdom = melhores_individuos[i]
        dados = []
        dados_values = []
        for j in range(len(values_subdom[0])):
            individuo = [subdom[k][j] for k in range(len(subdom))]
            dados.append(individuo)
            dados_values.append(values_subdom[j])
        todos_inds.append(dados)
        todos_inds_values.append(dados_values)
    # plot all
    for subdivisao in todos_inds:
        #select a random color
        color = [random.random(),random.random(),random.random()]
        for individuo in subdivisao:
            legend = "individuo "+str(j)
            values_plot = todos_inds_values[i][j]
            #var_1 = [values_plot[k][0] for k in range(len(values_plot))]
            #var_2 = [values_plot[k][1] for k in range(len(values_plot))]
            plt.plot(individuo, color=color, linewidth=0.5, alpha=0.7)
    # x axis
    plt.xlabel("Nº da geração")
    # y axis
    plt.ylabel("Avaliação")
    plt.show()

    x = [1+0.3*i for i in range(15)]
    y = [potential(45, 0.5, 3, value) for value in x]
    plt.plot(x, y, color="blue", linewidth=1.5, alpha=0.7)
    for subdivisao in melhores_individuos:
        # generate a random color for pyploy
        color = [random.random(),random.random(),random.random()]
        count_ind = 0
        for indivisuo in subdivisao:
            count_ind += 1
            x_new = [1+0.003*i for i in range(1500)]
            y_new = [potential(indivisuo[0], indivisuo[1], indivisuo[2], value) for value in x_new]
            linewidth = 0.5
            alpha = 0.5

            plt.plot(x_new, y_new, color=color, linewidth=linewidth, alpha=alpha)
    plt.show()

            
        

    print("avaliacoes")

