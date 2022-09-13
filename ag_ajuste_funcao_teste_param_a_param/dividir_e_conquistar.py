import re
import threading
from ga import GA
import datetime
import time

#ranges = [[2.5, 3.125], [0.0, 0.3125], [-0.625, 0.0], [0.0, 0.625], [0.125, 0.25]]
#ranges = [[-10,10],[-10,10],[-10,10],[-10,10],[-10,10]]
#ranges = [[0, 1000], [0, 300], [0, 200], [0, 200]]
#ranges = [[2, 10],[-5, 5],[-5, 5],[-10, 10],[1.3,1.6]]
#ranges = [[2.0, 4.612244897959183], [-0.10204081632653073, 1.7346938775510203], [1.44, 1.46]]
#ranges = [[0,100],[-50,50],[-50,50]]
#ranges = [[0.0, 14.285714285714286], [-7.142857142857146, 35.71428571428571], [-7.142857142857146, 35.71428571428571]]
#ranges = [[0.0, 2.0408163265306123], [-2.769679300291548, 5.102040816326527], [-1.0204081632653095, 5.102040816326527]]
ranges = [[0,10], [-10,10], [-10,10], [-10,10], [-10,10]]



def add_and_reorder(data, divisor, file_name, reverse):

    #print(data)
    # save on file file_name
    with open(file_name, "a") as f:
        for i in range(len(data)):
            value = [str(data[i][j]) for j in range(len(data[i]))]
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
    # remove all testes with 'e-'
    testes = [testes[i] for i in range(len(testes)) if not re.search("e-", testes[i][0])]
    # order testes by id
    testes = sorted(testes, key=lambda x: float(x[0]), reverse=reverse)
    # get the last 1000 testes
    testes = testes[:1000]

    # save on file file_name
    with open(file_name, "w") as f:
        for i in range(len(testes)):
            f.write(str(testes[i][0])+divisor+str(testes[i][1])+"\n")


def limites_espalhamento(limites, spaces):
    ranges = []
    for i in range(spaces):
        for j in range(spaces):
            for k in range(spaces):
                for l in range(spaces):
                    for m in range(spaces):
                        limites_var = []
                        limites_var.append([limites[0][0]+i*(limites[0][1]-limites[0][0]) / spaces, limites[0][0]+(i+1)*(limites[0][1]-limites[0][0])/spaces])
                        limites_var.append([limites[1][0]+j*(limites[1][1]-limites[1][0]) / spaces, limites[1][0]+(j+1)*(limites[1][1]-limites[1][0])/spaces])
                        limites_var.append([limites[2][0]+k*(limites[2][1]-limites[2][0]) / spaces, limites[2][0]+(k+1)*(limites[2][1]-limites[2][0])/spaces])
                        limites_var.append([limites[3][0]+l*(limites[3][1]-limites[3][0]) / spaces, limites[3][0]+(l+1)*(limites[3][1]-limites[3][0])/spaces])
                        limites_var.append([limites[4][0]+m*(limites[4][1]-limites[4][0]) / spaces, limites[4][0]+(m+1)*(limites[4][1]-limites[4][0])/spaces])
                        ranges.append(limites_var)
    return ranges




def executa_ga(geracoes, limite, avaliacoes, N=0):
    ga = GA(geracoes, limite, N=N)
    avaliacoes.append([ga.best_evaluation, limite])
    print("best_evaluation: ", ga.best_evaluation, "limite: ", limite)
    #write_on_file("avaliacoes_boas_dividir_conquistar.csv", ga.best_evaluation, limite)


def write_on_file(file_name, best_evaluation, limite):
    time = datetime.datetime.now()
    with open(file_name, "a") as f:
        datetime_now = datetime.datetime.now()
        datetime_now = datetime_now.strftime("%Y%m%d%H%M%S")
        date_interval = datetime.datetime.now() - time
        date_interval = date_interval.total_seconds()
        f.write(str(best_evaluation) + ";" + str(limite)+ ";"+ datetime_now + "\n")


    


inicio_da_execucao = datetime.datetime.now()


def exec_thread(limites, n_geracoes, N = 0):
    threads = []
    avaliacoes = []
    n__ = int(len(limites))
    
    for i in range(n__):
        results = [0] * n__
        
        threads.append(threading.Thread(target=executa_ga,
                       args=(n_geracoes, limites[i], avaliacoes, N)))

    i = 0
    for thread in threads:
        i += 1
        date_hour_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Thread "+str(i)+" started at "+date_hour_str)
        time.sleep(1)
        thread.start()
    for thread in threads:
        thread.join()

    add_and_reorder(avaliacoes, " -------- ", "testesss.log", True)

    # order avaliacoes by best_evaluation
    avaliacoes.sort(key=lambda x: x[0])
    print(avaliacoes[0][0])

    print(avaliacoes)
    tempo_fim_execucao = datetime.datetime.now()
    tempo_execucao = (tempo_fim_execucao - inicio_da_execucao).total_seconds()
    print("Tempo de execução: "+str(tempo_execucao)+" segundos")
    with open("esp_dom.log", "a") as f:
        f.write("Tempo de execução: "+str(tempo_execucao)+" segundos\n")
        f.write("----------------------\n")
    return avaliacoes

def get_best_limits(best):
    

    import csv
    import sys

    # read file with delimiter " ---- "
    with open("count.csv", "r") as f:
        # read data as array
        testes = f.readlines()
        # remove \n from each element of array
        testes = [testes[i].replace("\n", "") for i in range(len(testes))]
        # split each element of array by " -------- "
        testes = [testes[i].split(" ---- ") for i in range(len(testes))]
        # sort array by second element of each element
        testes.sort(key=lambda x: float(x[1]), reverse=False)
        # print array

    print(testes)
    testes = testes[0:best]
    limites = []
    for values in testes:
        
        limite = values[2]
        #remove first [ and last ]
        limite = limite[2:-2]
        #split by ,
        limite = limite.split("], [")
        limites_float = []
        for i in limite:
            #split by ,
            i = i.split(", ")
            #convert to float
            i = [float(j) for j in i]
            limites_float.append(i)
        # list of list of float
        limites.append(limites_float)

    new_limites = []
    for i in range(limites[0].__len__()):
        new_lim = [min([j[i][0] for j in limites]), max([j[i][1] for j in limites])]
        new_limites.append(new_lim)

    return new_limites

limites = limites_espalhamento(ranges, 3)
half_len = int(len(limites)/2)

avaliacoes_finais = []
avaliacoes = []
# executa a busca nos 32 limites
n_geracoes = 10
# N individuos
N = 500
#avaliacoes = exec_thread(limites, n_geracoes, N = N)
while True:
    new_limites = get_best_limits(3)
    limites = limites_espalhamento(new_limites, 3)
    avaliacoes = exec_thread(limites, n_geracoes, N = N)
    
    


