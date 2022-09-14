import re
import threading
from ga import GA
import datetime
import time

#ranges = [[2.5, 3.125], [0.0, 0.3125], [-0.625, 0.0], [0.0, 0.625], [0.125, 0.25]]
#ranges = [[-10,10],[-10,10],[-10,10],[-10,10],[-10,10]]
#ranges = [[0, 1000], [0, 300], [0, 200], [0, 200]]
#ranges = [[2, 10],[-5, 5],[-5, 5],[-10, 10],[1.3,1.6]]
ranges = [[2.0, 4.612244897959183], [-0.10204081632653073, 1.7346938775510203], [-5.0, 3.571428571428571], [-2.2448979591836733, 3.8775510204081636], [1.44, 1.46]]


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
    # ranges = [[[-1000,0,],[-1000,0,],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]]]
    esp_dom = [True, True, True, True, False]
    for i in range(spaces):
        for j in range(spaces):
            # i for element 0
            for k in range(spaces):
                for l in range(spaces):
                    if esp_dom[4]:
                        for m in range(spaces):
                            limites_var = []
                            limites_var.append([limites[0][0]+i*(limites[0][1]-limites[0][0]) / spaces, limites[0][0]+(i+1)*(limites[0][1]-limites[0][0])/spaces])
                            limites_var.append([limites[1][0]+j*(limites[1][1]-limites[1][0]) / spaces, limites[1][0]+(j+1)*(limites[1][1]-limites[1][0])/spaces])
                            limites_var.append([limites[2][0]+k*(limites[2][1]-limites[2][0]) / spaces, limites[2][0]+(k+1)*(limites[2][1]-limites[2][0])/spaces])
                            limites_var.append([limites[3][0]+l*(limites[3][1]-limites[3][0]) / spaces, limites[3][0]+(l+1)*(limites[3][1]-limites[3][0])/spaces])
                            limites_var.append([limites[4][0]+m*(limites[4][1]-limites[4][0]) / spaces, limites[4][0]+(m+1)*(limites[4][1]-limites[4][0])/spaces])
                            ranges.append(limites_var)
                    else:
                        limites_var = []
                        limites_var.append([limites[0][0]+i*(limites[0][1]-limites[0][0]) / spaces, limites[0][0]+(i+1)*(limites[0][1]-limites[0][0])/spaces])
                        limites_var.append([limites[1][0]+j*(limites[1][1]-limites[1][0]) / spaces, limites[1][0]+(j+1)*(limites[1][1]-limites[1][0])/spaces])
                        limites_var.append([limites[2][0]+k*(limites[2][1]-limites[2][0]) / spaces, limites[2][0]+(k+1)*(limites[2][1]-limites[2][0])/spaces])
                        limites_var.append([limites[3][0]+l*(limites[3][1]-limites[3][0]) / spaces, limites[3][0]+(l+1)*(limites[3][1]-limites[3][0])/spaces])
                        limites_var.append([limites[4][0], limites[4][1]])
                        ranges.append(limites_var)
    
    return ranges




def executa_ga(geracoes, limite, avaliacoes, N=0):
    ga = GA(geracoes, limite, N=N)
    avaliacoes.append([ga.best_evaluation, limite])
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
        time.sleep(0.1)
        thread.start()
    for thread in threads:
        time.sleep(0.1)
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


limites = limites_espalhamento(ranges, 7)
half_len = int(len(limites)/2)

avaliacoes_finais = []
avaliacoes = []
# executa a busca nos 32 limites
n_geracoes = 3
# N individuos
N = 300
avaliacoes += exec_thread(limites, n_geracoes, N = N)
avaliacoes.sort(key=lambda x: x[0])
limites = [avaliacoes[j][1] for j in range(4)]    
storage_avaliacao = []
for dividir in range(10):
    last_best = 4
    avaliacoes_last_best = avaliacoes[0:last_best]
    avaliacoes = []
    for i in range(last_best):
        limites = limites_espalhamento(avaliacoes_last_best[i][1], 7)
        avaliacoes += exec_thread(limites, n_geracoes, N = N)
        print("jaja")
    avaliacoes.sort(key=lambda x: x[0])


