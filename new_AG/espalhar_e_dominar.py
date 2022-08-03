import threading
from ga import GA
import datetime

ranges = [[-1000,1000],[0,10],[-1000,1000],[-1000,1000],[0,4]]

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

limites = limites_espalhamento(ranges,2)

def executa_ga(geracoes, limite):
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
    


threads = []
avaliacoes = []
n__ = int(len(limites))
for i in range(n__):
    results = [0] * n__
    threads.append(threading.Thread(target=executa_ga, args=(50, limites[i])))
    
    

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# order avaliacoes by best_evaluation
avaliacoes.sort(key=lambda x: x[0])

# select the first half
avaliacoes = avaliacoes[:4]

print(avaliacoes)

