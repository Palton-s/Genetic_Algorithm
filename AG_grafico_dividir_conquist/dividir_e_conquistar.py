import re
import threading
from ga import GA
import datetime
import json
import numpy as np
#ranges = [[2.5, 3.125], [0.0, 0.3125], [-0.625, 0.0], [0.0, 0.625], [0.125, 0.25]]
#ranges = [[-10,10],[-10,10],[-10,10],[-10,10],[-10,10]]
#ranges = [[-100,100],[0,10],[-100,100],[-100,100],[0,10]]
#ranges = [[5/6,2.5],[5/6,2.5]]


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









def add_and_reorder_json(file_name, data):
    #read json file_name
    with open(file_name, "r") as f:
        json_data = json.load(f)
    # add data to json_data
    json_data.append(data)
    # sort json_data by [0] from bigger to smaller
    json_data = sorted(json_data, key=lambda x: x[0], reverse=True)
    # save json_data on file_name
    with open(file_name, "w") as f:
        json.dump(json_data, f)
    return json_data

def get_best_limits(file_name):
    #read json file_name
    with open(file_name, "r") as f:
        json_data = json.load(f)
    limites = []
    # order json_data by [0]
    json_data = sorted(json_data, key=lambda x: x[0], reverse=True)
    # get the 5 first elements of json_data
    #bests = [json_data[0]]
    bests = json_data[0:3]
    limites = [[min(bests[j][1][i][0] for j in range(len(bests))), max(bests[j][1][i][1] for j in range(len(bests)))] for i in range(len(json_data[0][1]))]
    return limites

def limites_espalhamento(limites, spaces):
    ranges = []
    # ranges = [[[-1000,0,],[-1000,0,],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]]]
    for i in range(spaces):
        for j in range(spaces):
            limites_var = []
            limites_var.append([limites[0][0]+i*(limites[0][1]-limites[0][0])/spaces,limites[0][0]+(i+1)*(limites[0][1]-limites[0][0])/spaces])
            limites_var.append([limites[1][0]+j*(limites[1][1]-limites[1][0])/spaces,limites[1][0]+(j+1)*(limites[1][1]-limites[1][0])/spaces])
            ranges.append(limites_var)
    return ranges

def executa_ga(geracoes, limite,avaliacoes, melhores_valores):
    ga = GA(geracoes, limite)
    avaliacoes.append(ga.avaliacoes)
    melhores_valores.append(ga.melhores_valores)

inicio_da_execucao = datetime.datetime.now()
def exec_thread(limites, n_geracoes):
    threads = []
    avaliacoes = []
    melhores_valores = []
    n__ = int(len(limites))
    date_hour_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for i in range(n__):
        print("Thread "+str(i)+" started at "+date_hour_str)
        results = [0] * n__
        threads.append(threading.Thread(target=executa_ga, args=(n_geracoes, limites[i],avaliacoes, melhores_valores)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    limites_avaliacoes = []
    for i in range(len(limites)):
        limites_avaliacoes.append([avaliacoes[i][-1][0], limites[i]])
    for lim__ in limites_avaliacoes:
        add_and_reorder_json("avaliacoes_doms.json", lim__)
    """#add_and_reorder(avaliacoes, " -------- ", "testesss.log", True)

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
    return [avaliacoes, melhores_valores]"""

import matplotlib.pyplot as plt
import random

ranges = [[-6,2],[-6,2]]
limites = limites_espalhamento(ranges,4)
#limites = [[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]],[[-2.5,2.5],[-2.5,2.5]]]
half_len = int(len(limites)/2)
best_limits_for_graph = [ranges]
jaja = True
for i in range(10):
    avaliacoes_finais = []
    avaliacoes = []
    n_geracoes = 3
    #avaliacoes += exec_thread(limites,n_geracoes)
    thr = exec_thread(limites,n_geracoes)
    ranges = get_best_limits("avaliacoes_doms.json")
    best_limits_for_graph.append(ranges)
    limites = limites_espalhamento(ranges,4)

#plot line limites[i][0]

print(best_limits_for_graph)
var_1 = [best_limits_for_graph[i][0] for i in range(len(best_limits_for_graph))]
var_2 = [best_limits_for_graph[i][1] for i in range(len(best_limits_for_graph))]

line_inf_var_1 = [var_1[i][0] for i in range(len(var_1))]
line_sup_var_1 = [var_1[i][1] for i in range(len(var_1))]
line_inf_var_2 = [var_2[i][0] for i in range(len(var_2))]
line_sup_var_2 = [var_2[i][1] for i in range(len(var_2))]


# plot var1 lines
plt.plot(line_inf_var_1, color='red', label='Limite inferior x')
plt.plot(line_sup_var_1, color='green', label='Limite superior x')
plt.show()
# plot var2 lines
plt.plot(line_inf_var_2, color='red', label='Limite inferior y')
plt.plot(line_sup_var_2, color='green', label='Limite superior y')
plt.show()




"""    avaliacoes += thr[0]
    melhores_individuos = thr[1]
    todos_inds = []
    todos_inds_values = []
    for i in range(len(avaliacoes)):
        subdom = avaliacoes[i]
        values_subdom = melhores_individuos[i]
        dados = []
        dados_values = []
        for j in range(len(values_subdom)):
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
            
        

    print("avaliacoes")"""
