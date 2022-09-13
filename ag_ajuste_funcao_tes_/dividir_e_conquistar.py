import threading
from ga import GA
import datetime

#ranges = [[2.5, 3.125], [0.0, 0.3125], [-0.625, 0.0], [0.0, 0.625], [0.125, 0.25]]
#ranges = [[-10,10],[-10,10],[-10,10],[-10,10],[-10,10]]



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
    testes = sorted(testes, key=lambda x: float(x[0]), reverse=reverse)
    # get the last 1000 testes
    testes = testes[:1000]

    # save on file file_name
    with open(file_name, "w") as f:
        for i in range(len(testes)):
            string = [peace for peace in testes[i]]
            string = divisor.join(string)
            f.write(string+"\n")


def limites_espalhamento(limites, spaces):
    ranges = []
    # ranges = [[[-1000,0,],[-1000,0,],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]],[[-1000,0],[-1000,0],[-1000,0],[-1000,0],[-1000,0]],[[0,1000],[0,1000],[0,1000],[0,1000],[0,1000]]]
    for i in range(spaces):
        for j in range(spaces):
            # i for element 0
            for k in range(spaces):
                limites_var = []
                limites_var.append([limites[0][0]+i*(limites[0][1]-limites[0][0]) / spaces, limites[0][0]+(i+1)*(limites[0][1]-limites[0][0])/spaces])
                limites_var.append([limites[1][0]+j*(limites[1][1]-limites[1][0]) / spaces, limites[1][0]+(j+1)*(limites[1][1]-limites[1][0])/spaces])
                limites_var.append([limites[2][0]+k*(limites[2][1]-limites[2][0]) / spaces, limites[2][0]+(k+1)*(limites[2][1]-limites[2][0])/spaces])
                
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
        threads.append(threading.Thread(target=executa_ga,
                       args=(n_geracoes, limites[i], avaliacoes, N)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    add_and_reorder(avaliacoes, " -------- ", "conq_testesss.log", True)

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

def select_new_limites(limites):
    new_limites = []
    for i in range(len(limites[0])):
        new_lim_beg = min([limites[j][i][0] for j in range(len(limites))])
        new_lim_end = max([limites[j][i][1] for j in range(len(limites))])
        new_limites.append([new_lim_beg, new_lim_end])
    return new_limites

"""limites = limites_espalhamento(ranges, 2)
init_len = len(limites)

avaliacoes_finais = []
avaliacoes = []
# executa a busca nos 32 limites
n_geracoes = 50
N = 100
avaliacoes += exec_thread(limites, n_geracoes, N = N)
avaliacoes.sort(key=lambda x: x[0])
limites = [avaliacoes[j][1] for j in range(int(init_len/2))]
limites = select_new_limites(limites)
storage_avaliacao = []
for dividir in range(10000):
    last_best = 4
    avaliacoes_last_best = avaliacoes[0:last_best]
    avaliacoes = []
    for i in range(last_best):
        limites = limites_espalhamento(avaliacoes_last_best[i][1], 2)
        avaliacoes += exec_thread(limites, n_geracoes, N = N)
        print("jaja")
    avaliacoes.sort(key=lambda x: x[0])"""


limite = [[0, 128], [1, 128], [0, 128]]

n_geracoes = 2
N = 100

for rodada in range(1000):
    limites = limites_espalhamento(limite, 5)
    avaliacoes = []
    avaliacoes += exec_thread(limites, N = N, n_geracoes=n_geracoes)
    avaliacoes.sort(key=lambda x: x[0])
    limite = select_new_limites([avaliacoes[j][1] for j in range(int(len(limites)/4))])

