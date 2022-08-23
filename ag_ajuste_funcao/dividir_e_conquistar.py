import re
import threading
from ga import GA
import datetime

#ranges = [[2.5, 3.125], [0.0, 0.3125], [-0.625, 0.0], [0.0, 0.625], [0.125, 0.25]]
#ranges = [[-10,10],[-10,10],[-10,10],[-10,10],[-10,10]]
ranges = [[0, 1000], [0, 300], [0, 200], [0, 200]]


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
                        for variavel in range(len(limites)):
                            limites_var.append([limites[variavel][0]+i*(limites[variavel][1]-limites[variavel][0]) /
                                               spaces, limites[variavel][0]+(i+1)*(limites[variavel][1]-limites[variavel][0])/spaces])
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
    date_hour_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for i in range(n__):
        print("Thread "+str(i)+" started at "+date_hour_str)
        results = [0] * n__
        threads.append(threading.Thread(target=executa_ga,
                       args=(n_geracoes, limites[i], avaliacoes, N)))

    for thread in threads:
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


limites = limites_espalhamento(ranges, 2)
half_len = int(len(limites)/2)

avaliacoes_finais = []
avaliacoes = []
# executa a busca nos 32 limites
n_geracoes = 10
avaliacoes += exec_thread(limites, n_geracoes)
avaliacoes.sort(key=lambda x: x[0])
limites = [avaliacoes[j][1] for j in range(4)]    
while True:
    limites = limites_espalhamento(avaliacoes[0][1], 2)
    avaliacoes = []
    n_geracoes = 10
    avaliacoes += exec_thread(limites, n_geracoes, N = 1000)
    avaliacoes.sort(key=lambda x: x[0])
    print("jaja")
