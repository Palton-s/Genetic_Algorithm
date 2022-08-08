import re
import threading
from ga import GA
import datetime

#ranges = [[2.5, 3.125], [0.0, 0.3125], [-0.625, 0.0], [0.0, 0.625], [0.125, 0.25]]
#ranges = [[-10,10],[-10,10],[-10,10],[-10,10],[-10,10]]
ranges = [[-100,100],[0,10],[-100,100],[-100,100],[0,10]]

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

def limites_espalhamento(limites, spaces):
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
    return ranges



def executa_ga(geracoes, limite,avaliacoes):
    time = datetime.datetime.now()
    ga = GA(geracoes, limite)
    avaliacoes.append([ga.best_evaluation, limite])
    with open("esp_dom.log", "a") as f:
        # datetime format date and hour
        datetime_now = datetime.datetime.now()
        datetime_now = datetime_now.strftime("%Y-%m-%d %H:%M:%S")
        date_interval = datetime.datetime.now() - time
        date_interval = date_interval.total_seconds()
        f.write(" --------- "+datetime_now+" --------- "+str(int(date_interval))+" seconds -------- ")
        f.write(str(ga.best_evaluation) + " " + str(limite) + "\n")
    
    
        



inicio_da_execucao = datetime.datetime.now()
def exec_thread(limites, n_geracoes):
    threads = []
    avaliacoes = []
    n__ = int(len(limites))
    date_hour_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for i in range(n__):
        print("Thread "+str(i)+" started at "+date_hour_str)
        results = [0] * n__
        threads.append(threading.Thread(target=executa_ga, args=(n_geracoes, limites[i],avaliacoes)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    add_and_reorder(avaliacoes, " -------- ", "testesss.log", True)

    # order avaliacoes by best_evaluation
    avaliacoes.sort(key=lambda x: x[0])
    print(avaliacoes[0][0])

    # select the first half
    avaliacoes = avaliacoes[:4]

    print(avaliacoes)
    tempo_fim_execucao = datetime.datetime.now()
    tempo_execucao = (tempo_fim_execucao - inicio_da_execucao).total_seconds()
    print("Tempo de execução: "+str(tempo_execucao)+" segundos")
    with open("esp_dom.log", "a") as f:
        f.write("Tempo de execução: "+str(tempo_execucao)+" segundos\n")
        f.write("----------------------\n")
    return avaliacoes

limites = limites_espalhamento(ranges,3)
half_len = int(len(limites)/2)
while True:
    avaliacoes_finais = []
    avaliacoes = []
    for i in range(8):
        n_geracoes = 3
        avaliacoes += exec_thread(limites,n_geracoes)
        avaliacoes.sort(key=lambda x: x[0])
        limites = [avaliacoes[i][1] for i in range(4)]
    avaliacoes.sort(key=lambda x: x[0], reverse=True)
    avaliacoes.sort(key=lambda x: x[0])
    melhor_limite = avaliacoes[0][1]
    limites = limites_espalhamento(melhor_limite,2)